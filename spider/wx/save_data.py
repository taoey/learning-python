#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import spider.wx.mysql


def get_day_list(filepath):
    """每日文章列表"""
    with open(filepath, "r", encoding='UTF-8') as f:
        load_json = json.load(f)
        content = load_json.get("general_msg_list")
        content_dict = json.loads(content)
        content_list = content_dict.get("list")
        return content_list


def get_article_list(day_data):
    """处理单独一天的数据"""
    res = []
    art_datetime = day_data["comm_msg_info"].get("datetime", 0)
    # 首个文章
    first_item = {
        "title": day_data["app_msg_ext_info"]["title"],
        "digest": day_data["app_msg_ext_info"]["digest"],
        "content_url": day_data["app_msg_ext_info"]["content_url"],
        "cover": day_data["app_msg_ext_info"]["cover"],
        "article_date": art_datetime,
        "article_type": 0,  # 标注为首篇文章
        "create_time": datetime.now()
    }
    if len(first_item["digest"]) > 200: first_item["digest"] = first_item["digest"][0:200]
    res.append(first_item)
    # 是否有其他文章
    is_multi = int(day_data["app_msg_ext_info"]["is_multi"])
    if is_multi != 1: return res

    # 其他文章
    muti = day_data["app_msg_ext_info"]["multi_app_msg_item_list"]
    for sub in muti:
        sub_item = {
            "title": sub['title'],
            "digest": sub['digest'][0:200] if len(sub['digest']) > 200 else sub['digest'],
                       "content_url": sub['content_url'],
            "cover": sub['cover'],
            "article_date": art_datetime,
            "article_type": 1,
            "create_time": datetime.now()
        }
        res.append(sub_item)
    return res


def get_data_filepaths(dir):
    """
    获取数据文件绝对路径
    root :当前目录路径
    dirs:当前路径下所有子目录
    files:当前路径下所有非目录子文件
    """
    filepaths = []
    for root, dirs, files in os.walk(dir):
        for i in files:
            filepaths.append(dir + "/" + i)
    return filepaths


if __name__ == '__main__':
    paths = get_data_filepaths("data")
    for path in paths:
        print("--------------正在处理：-------------", path)
        day_list = get_day_list(path)
        for i in day_list:
            day_arts = get_article_list(i)
            for item in day_arts:
                if spider.wx.mysql.is_exist_by_content_url(item["content_url"]):
                    print(item["title"], "已经存在")
                    continue
                spider.wx.mysql.add(**item)
                print(item["title"], "保存成功")

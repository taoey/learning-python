#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time

from lxml import etree

from mysql import add


def select_data(page_source, tag):
    selector = etree.HTML(page_source)
    try:
        # 获取全部图片
        nodes = selector.xpath('//*[@class="media-content"]')

        res = []
        for node in nodes:
            title = node.xpath('@title')[0]
            url = node.xpath('@href')[0]
            res.append({
                "title": title,
                "url": url,
                "tag": tag
            })
        return res
    except:
        return []


def get_items():
    """获取所有相册集合数据"""
    # 获取html
    tags = ["二次元", "初恋", "古风", "可爱", "唯美", "回忆", "复古", "女神", "妹纸", "beauty", "小清新", "小王子", "少女", "尤克里里", "幽默", "心情",
            "情感", "摄影", "摄影写真", "文艺", "日系", "林小倩", "梦", "森女", "森系", "樱花", "汤音璇", "清纯", "爱情", "甜美", "短句", "私房", "程熙媛",
            "网络语", "翠花", "胶片", "greentea", "萝莉", "蔷薇", "读书", "轻私房", "钟曼菲", "随笔", "青春"]
    for tag in tags:
        with open(f"data/{tag}", 'r', encoding="utf-8") as f:
            content = f.read()
            res = select_data(content, tag)
            save_items_to_mysql(res)


def save_items_to_mysql(items):
    """存储相册数据到MySQL"""
    for i, item in enumerate(items):
        try:
            add(**item)
            time.sleep(0.5)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    get_items()

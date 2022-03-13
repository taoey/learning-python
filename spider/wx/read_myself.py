#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time

from spider.wx.mysql import is_exist_by_content_url, add
from spider.wx.save_data import get_data_filepaths, get_day_list, get_article_list
from spider.wx.update_data import get_browser


def scroll_to_bottom(browser):
    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = browser.execute_script(js)

    while height < new_height:
        for i in range(height, new_height, random.randint(80, 120)):
            browser.execute_script('window.scrollTo(0, {})'.format(i))
            time.sleep(0.5)
        height = new_height
        time.sleep(random.randint(1, 3))
        new_height = browser.execute_script(js)


if __name__ == '__main__':
    paths = get_data_filepaths("myself")
    all_item = {}
    for path in paths:
        print("--------------正在处理：-------------", path)
        day_list = get_day_list(path)
        for i in day_list:
            day_arts = get_article_list(i)
            for item in day_arts:
                all_item[item.get("content_url")] = 1

    # 遍历访问
    browser = get_browser()
    count = 1
    for i in all_item:
        print(f"all:{len(all_item)}  current:{count}")
        count += 1
        browser.get(i)
        scroll_to_bottom(browser)

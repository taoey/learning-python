#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 保存图片资源到本地
import time

from mysql import get_unsave
from util import get_browser


def save_pics(items, browser):
    # 打开浏览器
    for item in items:
        url = item['url']
        browser.get(url)
        print(url)
        source = browser.page_source
        print(source)
        time.sleep(1)
    pass


if __name__ == '__main__':
    browser = get_browser()
    for i in range(1):
        unsave_items = get_unsave(1)
        save_pics(unsave_items, browser)
    print("图片采集完毕")
    # browser.close()

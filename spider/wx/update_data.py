#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import math
import random
import time
import urllib
import urllib.request
import urllib.parse

from lxml import etree
from selenium import webdriver
import spider.wx.mysql


def get_browser():
    """启动一个普通浏览器"""
    driver_path = "F:\\chromedriver.exe"
    # driver_path = r"/Users/tao/soft/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    return browser


def select_pics(page_source):
    selector = etree.HTML(page_source)

    try:
        # 获取全部图片
        content = selector.xpath('//*[@id="js_content"]')[0]
        main_pic_src = content.xpath("//img/@src")
        pic_list = []
        for i in main_pic_src:
            if i.find("https://mmbiz.qpic.cn") != -1:
                pic_list.append(i)

        pics_json = json.dumps(dict(pics=pic_list))
        return pics_json
    except:
        return "0"


def get_new_data(browser, content_url):
    browser.get(content_url)
    time.sleep(random.randint(3, 6))
    pics = select_pics(browser.page_source)
    return pics


if __name__ == '__main__':
    # 获取抓包文件路径
    browser = get_browser()
    contents = spider.wx.mysql.get_muti_undownload(1000)
    for item in contents:
        pics = get_new_data(browser, item["content_url"])
        if pics:
            print(pics)
            spider.wx.mysql.update(item["id"], pic_url=pics)
    browser.close()

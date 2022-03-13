#!/usr/bin/env python
# -*- coding: utf-8 -*-
import util
from lxml import etree
import json
import os


def select_pics(page_source):
    selector = etree.HTML(page_source)
    pics = []
    try:
        # 获取全部图片
        nodes = selector.xpath('//img[@onload]')

        for node in nodes:
            pic = node.xpath('@src')[0] if len(node.xpath('@src')) > 0 else ""
            alt = node.xpath('@alt')[0] if len(node.xpath('@alt')) > 0 else ""
            if alt == "" or alt == "RSS" or alt == '唯美女生': continue
            pics.append({
                "pics": pic.replace("//", "https://"),
                "tag": alt.replace("-唯美女生", ""),
            })
        return pics
    except Exception as e:
        print(e)
        return pics


if __name__ == '__main__':
    # 读取page url
    all_page_json = []
    with open('all_urls.json', 'r', encoding='utf-8') as f:
        all_page_json = json.load(fp=f)

    browser = util.get_browser(util.MAC_WEBDRIVER_PATH)

    index = 0
    for one_page in all_page_json:
        if index < 0: continue

        browser.get(one_page['url'])
        pics = select_pics(browser.page_source)

        page_dir = f"爬虫结果/{one_page['title']}"
        isExists = os.path.exists(page_dir)
        if not isExists: os.makedirs(page_dir)

        # 保存数据
        with open(f"爬虫结果/{one_page['title']}/data.json", "w") as f:
            one_page['images'] = pics
            f.write(json.dumps(one_page))
            f.flush()

        # 保存网页数据
        with open(f"爬虫结果/{one_page['title']}/page.html", "w") as f:
            f.write(browser.page_source)
            f.flush()

        index += 1
        print(f"-----------------已完成：{index} --------------------")

    browser.close()

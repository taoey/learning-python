#!/usr/bin/env python
# -*- coding: utf-8 -*-
import util


DOMAIN = "www.vmgirls.com"

if __name__ == '__main__':
    # 文件中读取根节点tag uri列表
    root_uri = []
    uri = "tag/%e4%ba%8c%e6%ac%a1%e5%85%83/"
    url = f"{DOMAIN}/{uri}"

    # 获取单个tag页面内容 进行解析

    url = 'https://www.vmgirls.com/tag/少女'
    # url = 'view-source:https://www.vmgirls.com/15444.html'
    browser = util.get_browser(util.MAC_WEBDRIVER_PATH)
    browser.get(url)
    print(browser.page_source)
    # browser.close()

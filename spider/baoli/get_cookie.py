#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import requests
import time


def get_cookie():
    url_1 = "https://www.polyt.cn"
    url_2 = "https://www.polyt.cn/choose/seat?showId=42337&projectId=561956346200780800&sectionId=42248"
    browser = util.get_browser(util.MAC_WEBDRIVER_PATH)

    browser.get(url_1)

    input("随便输入一个字符")

    browser.get(url_2)

    cookies = browser.get_cookies()

    return cookies


if __name__ == '__main__':

    url = "https://platformpcgateway.polyt.cn/api/1.0/seat/getSeatInfo"

    payload = "{\"sectionId\":\"42248\",\"showId\":\"42337\",\"projectId\":\"561956346200780800\",\"requestModel\":{\"applicationSource\":\"plat_pc\",\"current\":1,\"size\":10,\"atgc\":\"6de16e080fb81cedc88baccd395233aa\",\"utgc\":\"utoken\",\"timestamp\":1620044190439,\"applicationCode\":\"plat_pc\"}}"
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'Accept': 'application/json, text/plain, */*',
        'DNT': '1',
        'httpType': 'detail',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://www.polyt.cn',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.polyt.cn/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'Hm_lvt_0cb4627679a11906d6bf0ced685dc014=1620040231; loginSession=ebc2eaf4a366ea039628297236dee2b4&&457a2321bbbaabc3676d32c2d4145908; acw_tc=707c9fc916200435961934931e544f56a20082185b35675981461bd3690313; Hm_lpvt_0cb4627679a11906d6bf0ced685dc014=1620044190'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

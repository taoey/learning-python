#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import time

if __name__ == '__main__':

    url_1 = "https://www.polyt.cn"
    url_2 = "https://www.polyt.cn/choose/seat?showId=42337&projectId=561956346200780800&sectionId=42248"
    browser = util.get_browser(util.MAC_WEBDRIVER_PATH)

    browser.get(url_1)
    time.sleep(60*2)


    browser.get(url_2)

    cookies = browser.get_cookies()

    print(cookies)

    browser.close()




#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(executable_path=r"/usr/local/src/chromedriver",options=chrome_options)
    browser.get(url)
    print(browser.page_source)

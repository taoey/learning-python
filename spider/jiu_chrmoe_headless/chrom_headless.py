#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver


LINUX_WEBDRIVER_PATH = r"/usr/local/src/chromedriver"
MAC_WEBDRIVER_PATH = r"/Users/tao/soft/chromedriver"

def get_headless_browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(executable_path=MAC_WEBDRIVER_PATH, options=chrome_options)
    return browser


def get_browser():
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path=MAC_WEBDRIVER_PATH, options=chrome_options)
    return browser



if __name__ == '__main__':
    url = 'https://www.gangbao365.com/exp/hangsource/buy/picksource/list.do'
    browser = get_browser()
    browser.get(url)
    browser.find_element_by_xpath("//*[@id='pageno']").send_keys(12)
    element_go = browser.find_element_by_xpath("/html/body/div[8]/form/div[12]/table/tbody/tr/td[2]/div/div[2]/span[2]/input[2]")
    browser.execute_script("arguments[0].click();", element_go)
    # browser.find_element_by_xpath("/html/body/div[8]/form/div[12]/table/tbody/tr/td[2]/div/div[2]/a[8]").click()  # 下一页
    time.sleep(1)
    print(browser.page_source)

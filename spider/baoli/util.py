#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import os
import time
import urllib
from urllib.parse import unquote

import aiohttp
import requests

from PIL import Image
from selenium import webdriver

LINUX_WEBDRIVER_PATH = r"/usr/local/src/chromedriver"
MAC_WEBDRIVER_PATH = r"/Users/tao/soft/chromedriver_90"


def common_req(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    return res.text


def get_headless_browser(driver_path):
    """启动一个无头浏览器"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    return browser


def get_browser(driver_path=MAC_WEBDRIVER_PATH):
    """启动一个普通浏览器"""
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    return browser


def url_decode(url_str):
    return unquote(url_str, 'utf8')


def fullpage_screenshot(driver, file):
    print("Starting chrome full page screenshot workaround ...")

    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
    viewport_width = driver.execute_script("return document.body.clientWidth")
    viewport_height = driver.execute_script("return window.innerHeight")
    print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
    rectangles = []

    i = 0
    while i < total_height:
        ii = 0
        top_height = i + viewport_height

        if top_height > total_height:
            top_height = total_height

        while ii < total_width:
            top_width = ii + viewport_width

            if top_width > total_width:
                top_width = total_width

            print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
            rectangles.append((ii, i, top_width, top_height))

            ii = ii + viewport_width

        i = i + viewport_height

    stitched_image = Image.new('RGB', (total_width, total_height))
    previous = None
    part = 0

    for rectangle in rectangles:
        if not previous is None:
            driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
            print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
            time.sleep(0.2)

        file_name = "part_{0}.png".format(part)
        print("Capturing {0} ...".format(file_name))

        driver.get_screenshot_as_file(file_name)
        screenshot = Image.open(file_name)

        if rectangle[1] + viewport_height > total_height:
            offset = (rectangle[0], total_height - viewport_height)
        else:
            offset = (rectangle[0], rectangle[1])

        print("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
        stitched_image.paste(screenshot, offset)

        del screenshot
        os.remove(file_name)
        part = part + 1
        previous = rectangle

    stitched_image.save(file)
    print("Finishing chrome full page screenshot workaround...")
    return True


def client_post(url, data):
    url = "https://www.vmgirls.com/wp-admin/admin-ajax.php"
    data = {"key": "value"}
    res = requests.post(url=url, data=data)
    print(res.text)


async def main():
    http_client = aiohttp.ClientSession()
    url = "https://www.vmgirls.com/wp-admin/admin-ajax.php"
    data = {'append': 'list-archive',
            'paged': '1',
            'action': 'ajax_load_posts',
            'query': '少女',
            'page': 'tag'
            }
    async with http_client.post(url, data=data) as resp:
        t = await resp.text()
        print(t)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

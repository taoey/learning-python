#coding=utf-8
from selenium.webdriver import PhantomJS

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    browser = PhantomJS(executable_path=r'/usr/local/src/phantomjs')
    browser.get(url)
    print(browser.page_source)
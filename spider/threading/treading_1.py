#_*_coding:utf-8_*_
from multiprocessing import  Process,Manager
import os,time
from selenium import webdriver


def fun_1(list):
    chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS()

    driver.get("http://blog.sina.com.cn/u/5616913982")
    src=driver.page_source
    list.append(src)

def fun_2(list):
    chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS()

    driver.get("https://www.douban.com/")
    src=driver.page_source
    list.append(src)

def fun_3(list):
    chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS()

    driver.get("http://www.bilibili.com/")
    src=driver.page_source
    list.append(src)

if __name__ == '__main__':
    start=time.time()
    manger=Manager()
    l=manger.list()
    p=Process(target=fun_1,args=(l,))
    p2=Process(target=fun_2,args=(l,))
    p3 = Process(target=fun_3, args=(l,))

    p.start()
    p2.start()
    p3.start()

    p.join()
    p2.join()
    p3.join()
    print(len(l),l)
    end=time.time()
    print(end-start)


    #55.36027383804321
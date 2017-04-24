from selenium import webdriver
import os,time

if __name__ == '__main__':
    start=time.time()
    # chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
    # driver = webdriver.Firefox()
    #time=54.88944101333618

    chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    driver = webdriver.PhantomJS()
    #time=19.93502187728882

    url1="http://blog.sina.com.cn/u/5616913982"
    url2="https://www.douban.com/"
    url3="http://www.bilibili.com/"
    url_1 = 'https://search.jd.com/Search?keyword=%E6%9C%8D%E8%A3%' \
            '85&enc=utf-8&wq=%E6%9C%8D%E8%A3%85&pvid=12da848282864849ae3ceda2666c8b72'
    l=[url_1]
    r=[]
    for i in l:
        driver.get(i)
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        src=driver.page_source
        r.append(src)
    print(len(r),r)
    end=time.time()
    print(end-start)
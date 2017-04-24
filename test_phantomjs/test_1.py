from selenium import webdriver

url_1='https://search.jd.com/Search?keyword=%E6%9C%8D%E8%A3%' \
     '85&enc=utf-8&wq=%E6%9C%8D%E8%A3%85&pvid=12da848282864849ae3ceda2666c8b72'
chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
driver = webdriver.PhantomJS()
driver.set_page_load_timeout(5)
try:
    driver.get(url_1)
    print (driver.page_source)
except Exception as e:
    print (e)
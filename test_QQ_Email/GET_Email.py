from selenium import webdriver
from lxml import etree
import time


if __name__ == '__main__':

    chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
    driver = webdriver.Firefox()

    # chromedriver = "D:\CCApplication\phantomjs-2.1.1-windows\bin\phantomjs.exe"
    # driver = webdriver.PhantomJS()

    driver.get("http://qun.qq.com/member.html")

    IframeElement=driver.find_element_by_name("login_frame")
    driver.switch_to_frame(IframeElement)

    driver.find_element_by_xpath("//*[@id='bottom_qlogin']/a[1]").click()  # 登录界面
    driver.find_element_by_xpath("//*[@id='u']").send_keys("2517129987")
    driver.find_element_by_xpath("//*[@id='p']").send_keys("")    #输入你的密码

    driver.find_element_by_xpath("//*[@id='login_button']").click()  #点击登录
    time.sleep(2)


    driver.switch_to_default_content()  #防止出现TypeError: can't access dead object 错误特别重要
    print(driver.current_url)
    print(driver.page_source)

    web_data = driver.page_source
    selector = etree.HTML(web_data)

    qq_number=selector.xpath("//li[@data-id]/@data-id")         #获取所有的QQ群组号码和名称
    qq_name=selector.xpath("//li[@data-id]/@title")
    print(qq_number,qq_name)




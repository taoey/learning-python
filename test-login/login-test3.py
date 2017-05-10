'''
测试成功

模拟登录燕山大学图书馆系统(要求Windows系统有D盘)
'''
from selenium import webdriver
import time
import pytesseract
from PIL import Image
import urllib, urllib.request


def getpic(pic_url,cookie):
    '''
    带cookie访问验证码地址,以实现登录功能
    :param pic_url:
    :param cookie:
    :return:
    '''
    header={
        'Cookie':cookie,
    }
    requ = urllib.request.Request(pic_url,headers=header)
    try:
        imgData = urllib.request.urlopen(requ).read()
        with open('D:/'+'test.png', 'wb') as f:
            f.write(imgData)
            f.close()
        print('yes')
    except Exception as e:
        print(e)
        print('write error')

if __name__ == '__main__':

    url='http://202.206.242.99:8080/reader/redr_verify.php'
    check_url='http://202.206.242.99:8080/reader/captcha.php'
    driver=webdriver.Firefox()
    driver.get(url)

    #数据获取
    id=''                    #你的id卡号
    password=''              #你的密码
    cookie=driver.get_cookies()          #获取所有cookie信息
    #pirnt(cookie)
    cookie=cookie[0]['value']            #获取cookie信息(list->字典)
    getpic(check_url,'PHPSESSID='+cookie)
    image = Image.open('D:/test.png')
    vcode = pytesseract.image_to_string(image)

    #输入表单并提交
    driver.find_element_by_id('number').send_keys(id)
    driver.find_element_by_xpath("//*[@id='left_tab']/form/table/tbody/tr[2]/td[2]/input").send_keys(password)
    driver.find_element_by_id('captcha').send_keys(vcode)
    driver.find_element_by_xpath("//*[@id='left_tab']/form/table/tbody/tr[6]/td[2]/input[1]").click()










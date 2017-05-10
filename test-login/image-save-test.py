'''
测试成功
'''
import requests
import urllib, urllib.request


def getpic(pic_url):
    requ = urllib.request.Request(pic_url)
    try:
        imgData = urllib.request.urlopen(requ).read()
        with open('D:/'+pic_url[-7:]+'.png', 'wb') as f:
            f.write(imgData)
            f.close()
        print('yes')
    except Exception as e:
        print(e)
        print('write error')

def getpic2(pic_url,cookie):
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

pic_url='http://202.206.242.99:8080/reader/captcha.php'
getpic(pic_url)
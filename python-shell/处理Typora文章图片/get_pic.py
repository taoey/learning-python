import urllib
import urllib.request
import os

if __name__ == '__main__':
    cdir = os.getcwd()
    path = cdir+"\\"+"pic.jpg"
    url = 'http://pqkft7tpa.bkt.clouddn.com/%E6%B5%8B%E8%AF%95pic.jpg?imageView2/0/q/100|watermark/2/text/44CQ5b6u5L-h5YWs5LyX5Y-377ya5Z2C5pys5YWI55Sf44CR/font/6buR5L2T/fontsize/400/fill/IzNGOTREQQ==/dissolve/100/gravity/NorthEast/dx/10/dy/10'

    key = "测试pic.jpg"
    # 对中文进行编码（百分号编码）
    key = urllib.request.quote(key)
    pic_url = "http://pqkft7tpa.bkt.clouddn.com/" + key \
              + "?imageView2/0/q/100|watermark/2/text/44CQ5b6u5L-h5YWs5LyX5Y-377ya5Z2C5pys5YWI55Sf44CR/font/6buR5L2T/fontsize/400/fill/IzNGOTREQQ==/dissolve/100/gravity/NorthEast/dx/10/dy/10"
    print(pic_url)
    urllib.request.urlretrieve(pic_url, path)

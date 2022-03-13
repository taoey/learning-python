#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib
import urllib.request
import urllib.parse



def upload_to_qiniu(filepath):
    """上传文件到七牛云"""
    file_url = ""
    return file_url


def save_pic(pic_url, pathfile):
    # urllib.request.urlretrieve(imgurl, path)  # 打开imgList,下载图片到本地

    url = urllib.parse.parse_qs(urllib.parse.urlsplit(pic_url).query)
    pic_suf = url.get("wx_fmt")[0] if url.get("wx_fmt")[0] else "gif"
    filename = f"{int(time.time())}.{pic_suf}"

    Header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.87 Mobile Safari/537.36',
    }
    requ = urllib.request.Request(pic_url, headers=Header)
    try:
        imgData = urllib.request.urlopen(requ).read()
        with open(pathfile + filename, 'wb') as f:
            f.write(imgData)
            f.close()
        print(pathfile)
    except:
        print('write error' + pathfile + filename)
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from qiniu import Auth, put_file, PersistentFop, build_op, op_save, urlsafe_base64_encode
import os
from random import choice
from PIL import Image, ImageFont, ImageDraw, ImageSequence


def upload_img(file_name, file_path):
    """上传图片到七牛云"""
    access_key = "OcZiLE2w5HFn-piCno178aJ0g32pfI18bG4rjC7v"
    secret_key = "CrJjANFUyfSEFp36UsFXsi0DBiuZWL4H6rh_RIM5"

    q = Auth(access_key, secret_key)
    bucket_name = 'python_wx_pic'
    key = file_name
    token = q.upload_token(bucket_name, key, 3600)
    localfile = file_path
    ret, info = put_file(token, key, localfile)
    print(file_name, "上传成功")

    return ret["key"]


def get_suffix(file_path):
    """获取文件后缀"""
    sp_arr = file_path.split(".", 1)
    return sp_arr[1] if len(sp_arr) == 2 else ""


def add_gif_mask(text, file_path):
    pass





if __name__ == "__main__":
    pass

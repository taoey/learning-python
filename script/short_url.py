#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 62进制,特别合于月、日、时、分、秒的压缩进储
digit62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def int_to_str62(x):
    """整数转化为62进制字符串"""
    try:
        x = int(x)
    except:
        x = 0
    if x < 0:x = -x
    if x == 0:return "0"
    s = ""
    while x > 62:
        x1 = x % 62
        s = digit62[x1] + s
        x = x // 62   # 向下取整
    if x > 0: s = digit62[x] + s
    return s


def str62_to_int(s):
    """62进制字符串转化为整数"""
    x = 0
    s = str(s).strip()
    if s == "":return x
    for y in s:
        k = digit62.find(y)
        if k >= 0:
            x = x * 62 + k
    return x


"""短URL设计


"""

if __name__ == '__main__':
    x = 58
    s = int_to_str62(x)
    y = str62_to_int(s)
    print(x, s, y)

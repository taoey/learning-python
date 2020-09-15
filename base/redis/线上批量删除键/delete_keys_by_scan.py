#!/usr/bin/env python
# -*- coding: utf-8 -*-


import redis
import time

"""
scan命令的第一个入参从0开始代表从头扫描
scan命令的返回是(pos, [])元组，第一个pos可以作为下次扫描的入参pos，第二个值就是扫描到的KEY
scan命令的第三个参数，是本次扫描的KEY数目，比如传递10万个，但是返回的LIST可能是0，因为有0个匹配
redis的delete命令传递的是array参数，可以用*list传递
"""
client = redis.StrictRedis(host="127.0.0.1", port=6379)


def del_by_scan_keys(pattern):
    begin_pos = 0
    while True:
        result = client.scan(begin_pos, pattern, 10000)
        return_pos, datalist = result
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), return_pos)
        if len(datalist) > 0:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), "delete", len(datalist))
            client.delete(*datalist)
        if return_pos == 0:
            break
        begin_pos = return_pos
        time.sleep(1)
    print("over")


if __name__ == '__main__':
    del_by_scan_keys("tao_test_key1*")
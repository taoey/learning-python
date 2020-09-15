#!/usr/bin/env python
# -*- coding: utf-8 -*-


import redis
import time

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
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)

def run():
    start = time.time_ns()
    print(start)
    keys = client.keys("tao_test_key*")
    pipeline = client.pipeline(transaction=False)
    for key in keys:
        pipeline.delete(key.decode())
    pipeline.execute()
    end = time.time_ns()
    print((end-start)/10e6) # 3658.0457646


if __name__ == '__main__':
    run()
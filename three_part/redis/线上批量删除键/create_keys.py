#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)

A_HOUR = 3600


def create_keys(prefix, amount):
    pipe = client.pipeline(transaction=False)
    for i in range(amount):
        pipe.set(f"{prefix}_{i}",1,ex=A_HOUR)
    pipe.execute()
    time.sleep(0.5)


if __name__ == '__main__':
    create_keys("tao_test_key", 100000)
    create_keys("tao_test_key1", 200000)
    create_keys("tao_test_key2", 300000)
    create_keys("tao_test_key3", 400000)

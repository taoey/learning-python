#!/usr/bin/env python
# -*- coding: utf-8 -*-
import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)

def test_01():
    print("hello")
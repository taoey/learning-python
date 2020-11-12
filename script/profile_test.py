#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import random


def fun1():
    res = []
    max_len = 100000
    arr = [i for i in range(max_len)]
    for i in range(1000):
        cur = random.randint(0, max_len)
        if cur in arr:
            res.append(cur)
    return res


def fun2():
    res = []
    max_len = 100000
    arr = set([i for i in range(max_len)])
    for i in range(1000):
        cur = random.randint(0, max_len)
        if cur in arr:
            res.append(cur)
    return res


if __name__ == '__main__':
    print(fun1())
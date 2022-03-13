#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getMyArr(arr):
    result = []
    arr_min, arr_max = [], []
    min_num, max_num = 0, 10000
    for i in range(len(arr)):
        min_num = min(min_num, arr[i])
        arr_min[i] = min_num

    for i in range(len(arr)):
        max_num = max(max_num, arr[i])
        arr_max[i] = max_num

    for i in range(len(arr)):
        if arr[i] > arr_min[i] and arr[i] < arr_max[i]:
            result.append(arr[i])

    return result

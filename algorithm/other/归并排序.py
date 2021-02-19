#!/usr/bin/env python
# -*- coding: utf-8 -*-

def merge(a, b):
    res = []
    pa = pb = 0
    while pa < len(a) and pb < len(b):
        if a[pa] < b[pb]:
            res.append(a[pa])
            pa += 1
        else:
            res.append(b[pb])
            pb += 1
    if pa == len(a):
        for i in b[pb:]:
            res.append(i)
    else:
        for i in a[pa:]:
            res.append(i)

    return res


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(merge_sort(a))

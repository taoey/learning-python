#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

# 数据范围 10K
# 桶计数法
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        buckets = [0 for i in range(10001)]
        for cur in arr:
            buckets[cur] += 1
        res = []
        count = 0
        for index, item in enumerate(buckets):
            if item > 0:
                for i in range(item):
                    if count < k:
                        res.append(index)
                        count += 1

        return res

if __name__ == '__main__':
    arr = [0,1,2,1]
    s = Solution()
    res = s.getLeastNumbers(arr, 3)
    print(res)
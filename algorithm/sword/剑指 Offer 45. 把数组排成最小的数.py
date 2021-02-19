#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:
输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
"""
import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare_personal(x, y):
            m, n = x + y, y + x
            if m > n:
                return 1
            elif m < n:
                return -1
            else:
                return 0

        nums = [str(i) for i in nums]
        nums.sort(key=functools.cmp_to_key(compare_personal))
        print(nums)
        return "".join(nums)


if __name__ == '__main__':
    l = [3, 30, 34, 5, 9]
    s = Solution()
    number = s.minNumber(l)
    print(number)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        a = b =0
        # 求两个不同数字的异或值
        xor = 0
        for num in nums:
            xor ^= num
        # 找到异或值xor从右数第一位不为0的
        h = 1
        while xor & h == 0:
            h <<= 1
        # 分组
        for n in nums:
            if h & n == 0:
                a ^= n
            else:
                b ^= n
        # 每组求异或值
        return [a, b]


if __name__ == '__main__':
    arr = [1, 2, 10, 4, 1, 4, 3, 3]
    res = Solution().singleNumbers(arr)
    print(res)

    # aa = 1 ^ 3
    # mask = aa & (-aa)
    # print(mask)
    print(bin(4).replace('0b', ''))
    print(3 & -3)

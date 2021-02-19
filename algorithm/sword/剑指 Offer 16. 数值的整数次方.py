#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

输入: 2.00000, 10
输出: 1024.00000

解法： 快速幂
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    res = Solution().myPow(2.5, 2)
    print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
1 是丑数。
n 不超过1690。
"""

"""
动态规划题目
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        a = b = c = 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]


if __name__ == '__main__':
    res = Solution().nthUglyNumber(10)
    print(res)

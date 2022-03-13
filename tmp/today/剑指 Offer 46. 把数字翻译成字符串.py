#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

[1,2,2,5,8],[1,22,5,8],[1,2,25,8],[12,2,5,8],[12,25,8]
0 <= num < pow(2,23)
"""
"""
思路：超过25的组合不能输出

因此区间为 [10,25]
"""


class Solution:
    def translateNum(self, num: int) -> int:
        s_num = str(num)
        s_len = len(s_num)
        # 边界值判断
        if s_len <= 1: return 1

        cur = 1
        dp = [1] * s_len
        while cur < s_len:
            if "10" <= s_num[cur - 1:cur+1] <= "25":
                dp[cur] = dp[cur - 1] + dp[cur - 2]
            else:
                dp[cur] = dp[cur - 1]
            cur += 1
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    res = Solution().translateNum(12258)
    print(res)

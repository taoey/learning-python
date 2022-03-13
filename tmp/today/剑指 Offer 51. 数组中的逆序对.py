#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

[[7,5][7,6][7,4],[5,4],[6,4]]

动态规划：dp[i] = dp[i-1] + cur(i)
"""

"""
超时！！！ 相关测试用例：https://leetcode-cn.com/submissions/detail/137868964/testcase/
"""
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len <= 1: return 0
        dp = [0] * nums_len
        cur = 1
        while cur < nums_len:
            cur_num = 0
            for tmp in nums[:cur]:
                if tmp > nums[cur]: cur_num += 1
            dp[cur] = dp[cur - 1] + cur_num
            cur += 1
        return dp[-1]


if __name__ == '__main__':
    arr = [7, 5, 6, 4]
    res = Solution().reversePairs(arr)
    print(res)

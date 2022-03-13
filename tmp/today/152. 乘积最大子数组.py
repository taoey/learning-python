#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from typing import List

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""

"""
dp[i] = max(num,dp[i-1]*num)
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


if __name__ == '__main__':
    arr = [2, 3, -2, 4]
    res = Solution().maxProduct(arr)
    print(res)

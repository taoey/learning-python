#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
动态规划解法：

dp[i-1] > 0  : dp[i] = dp[i-1] + nums[i]
dp[i-1] <= 0 : dp[i] = nums[i]      (dp[i-1]对dp[i]产生副作用，故舍弃dp[i-1])

"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] if dp[i - 1] <= 0 else dp[i - 1] + nums[i]
        return max(dp)


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    max_num = s.maxSubArray(arr)
    print(max_num)

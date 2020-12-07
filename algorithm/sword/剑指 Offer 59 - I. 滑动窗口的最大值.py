#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue
from collections import deque
from typing import List


# 暴力解法：每次求对应的range的最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        return [max(nums[i:i+k]) for i in range(n-k+1)]


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    s = Solution()
    tar = s.maxSlidingWindow(nums, k)
    print(tar)

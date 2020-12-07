#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


"""
时间复杂度要求：log(n)

要是要求时间复杂度为logn，而且在有序数组中查找元素，那肯定是二分法呀
"""

class Solution:
    def searchLeft(self, nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return index

    def searchRight(self, nums, target):
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeft(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.searchRight(nums, target)
        return [left, right]

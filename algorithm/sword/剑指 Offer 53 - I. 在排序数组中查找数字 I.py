#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
统计一个数字在排序数组中出现的次数

二分查找的变形 原题leetcode54
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

    def search(self, nums: List[int], target: int) -> int:
        left = self.searchLeft(nums, target)
        if left == -1:
            return 0
        right = self.searchRight(nums, target)
        return right - left + 1

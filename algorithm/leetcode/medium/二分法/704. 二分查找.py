#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# nums = [-1,0,3,9,12], target = 9


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # （left + right）// 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == '__main__':
    nums = [2, 5, 5, 5, 6, 7]
    target = 5
    s = Solution()
    res = s.search(nums, target)



# 判断一个数是否在有序数组中
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        mid = (len(nums) - 1) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        else:
            return self.search(nums[mid + 1:], target)

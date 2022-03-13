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


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.sum = 0

        def merge(nums, start, mid, end):
            i, j, temp = start, mid + 1, []
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.sum += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1

            for i in range(len(temp)):
                nums[start + i] = temp[i]

        def mergeSort(nums, start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return self.sum


if __name__ == '__main__':
    arr = [7, 5, 6, 4]
    res = Solution().reversePairs(arr)
    print(res)

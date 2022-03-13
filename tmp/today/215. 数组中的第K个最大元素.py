#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

考察快速排序
"""

from typing import List


class Solution:
    def partition(self, arr, low, high):
        i = (low - 1)  # 最小元素索引
        pivot = arr[high]

        for j in range(low, high):
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums[-k]


if __name__ == '__main__':
    arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    res = Solution().findKthLargest(arr, 4)  # 4
    print(res)

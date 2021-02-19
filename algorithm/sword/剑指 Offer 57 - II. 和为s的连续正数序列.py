#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

"""
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target < 3: return
        left, right = 1, 2
        sum = 3  # 滑动窗口中数字的和
        res = []
        while left <= target // 2:
            if sum < target:
                # 右边界向右移动
                right += 1
                sum += right
            elif sum > target:
                # 左边界向右移动
                sum -= left
                left += 1
            elif sum == target:
                arr = list(range(left, right+1))
                res.append(arr)
                # 右边界向右移动
                right += 1
                sum += right
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.findContinuousSequence(9)
    print(res)

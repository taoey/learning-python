#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List



# 需要明确题目中 数据是否有序


# 通用做法：set判断

"""
直接用了python的set运算 感觉挺不要脸的
"""
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return set(nums1).intersection(set(nums2))

"""
使用set
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        if len(set_1)<len(set_2): # 取小集合进行遍历
            return [num for num in set_1 if num in set_2]
        else:
            return [num for num in set_2 if num in set_1]


if __name__ == '__main__':
    s = Solution()
    l1 =[1,23,4,5]
    l2 =[2,3,4,5]
    print(s.intersection(l1,l2))
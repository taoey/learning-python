#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        """
        0、判断是否递增
        1、判断最大值和最小值之差
        :param nums:
        :return:
        """
        repeat = set()
        for num in nums:
            if num == 0: continue
            if num not in repeat:
                repeat.add(num)
            else:
                return False

        return max(repeat) - min(repeat) <= 4

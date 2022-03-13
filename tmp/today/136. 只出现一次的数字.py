#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    arr = [2, 2, 1]
    res = Solution().singleNumber(arr)
    print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0: x = num
            votes += 1 if num == x else -1
        return x


if __name__ == '__main__':
    mylist = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    res = s.majorityElement(mylist)
    print(res)

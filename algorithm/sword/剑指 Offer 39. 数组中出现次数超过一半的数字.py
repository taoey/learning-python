#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 判空
        if not nums: return 0

        time = 0
        for cur in nums:
            if time == 0:
                time = 1
                res = cur
            elif cur == res:
                time += 1
            elif cur != res:
                time += -1
        # 判断所求数值是否符合要求:出现次数大于一半
        count = 0
        for item in nums:
            if item == res: count += 1
        return res if count * 2 >= time else 0


if __name__ == '__main__':
    mylist = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    s = Solution()
    res = s.majorityElement(mylist)
    print(res)

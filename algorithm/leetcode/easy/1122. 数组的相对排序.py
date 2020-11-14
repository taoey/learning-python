#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def mycmp(x):
            return arr_map[x] if x in arr_map else x
            pass

        # 建立映射,注意因为是正数，所以分为两部分，arr2中的数为负数，进行自定义排序的时候能够排在前面
        arr_len = len(arr2)
        arr_map = {item: index-arr_len for index, item in enumerate(arr2)}

        arr1.sort(key=mycmp)
        return arr1



if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]

    s = Solution()
    array = s.relativeSortArray(arr1, arr2)
    print(array)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def get_dis(self, r0, c0, r1, c1):
        return abs(r0 - r1) + abs(c0 - c1)

    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R):
            for j in range(C):
                res.append(([i, j], self.get_dis(r0, c0, i, j)))

        res.sort(key=lambda x: x[1])
        return [x[0] for x in res]


if __name__ == '__main__':
    s = Solution()
    res = s.allCellsDistOrder(R=4, C=4, r0=0, c0=0)
    print(res)

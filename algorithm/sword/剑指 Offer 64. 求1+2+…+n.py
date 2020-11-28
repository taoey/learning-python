#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n-1)
        self.res += n
        return self.res


if __name__ == '__main__':
    n = 3
    s = Solution()
    sum = s.sumNums(n)
    print(sum)
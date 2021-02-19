#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
考点：三次翻转字符串得到
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s1 = self.reverse_str(s, 0, n)
        s2 = self.reverse_str(s, n, len(s))
        s3 = self.reverse_str(s1+s2, 0, len(s))
        return s3

    def reverse_str(self, str, left, right):
        tmp = str[left:right]
        print("tao", tmp[::-1])
        return tmp[::-1]


if __name__ == '__main__':
    my_str = "abcdefg"
    k = 2
    s = Solution()

    res = s.reverseLeftWords(my_str, k)
    print(res)

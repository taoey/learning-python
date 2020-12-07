#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        left = right = len(s) - 1
        res = []
        while left >= 0:
            while left >= 0 and s[left] != " ": left -= 1
            res.append(s[left + 1:right + 1])
            while s[left] == " ": left -= 1
            right = left
        return res


if __name__ == '__main__':
    words = "  hello    world  "
    s = Solution()
    res = s.reverseWords(words)
    print(res)

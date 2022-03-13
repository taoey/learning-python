#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            #  分别拿到奇数偶数的回文子串长度
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            print(s[left1:right1 + 1], s[left2:right2 + 1])
            # 对比最大的长度
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


if __name__ == '__main__':
    s = "acc"
    res = Solution().longestPalindrome(s)
    print("res:", res)

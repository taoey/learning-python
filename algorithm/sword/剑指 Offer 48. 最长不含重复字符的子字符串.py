#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""

"""
滑动窗口
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        max_len = 1
        if len(s) < 2: return len(s)
        while right < len(s) - 1:
            right += 1
            if s[right] not in s[left:right]:
                max_len = max(right - left + 1, max_len)
            else:   # 当前元素已经重复，缩减窗口到无重复元素
                while s[right] in s[left:right]:
                    left += 1
        return max_len

if __name__ == '__main__':
    s = "bbbb"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)

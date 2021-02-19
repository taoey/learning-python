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
        dic = {}
        left, max_len = 0, 0
        for right in range(len(s)):
            # 如果说尾指针存在哈希表中，把头指针跳转到开始重复元素的上一位
            if s[right] in dic:
                left = max(dic[s[right]], left)
            # 更新哈希表
            dic[s[right]] = right + 1
            # 更新长度
            max_len = max(max_len, right - left + 1)
        return max_len


if __name__ == '__main__':
    s = "abca"
    res = Solution().lengthOfLongestSubstring(s)
    print(res)

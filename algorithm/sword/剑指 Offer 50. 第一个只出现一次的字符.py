#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
0 <= s 的长度 <= 50000
"""

"""
仅有26个字符,可以设置26个桶
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        count_dict = {}
        for i in s:
            if i in count_dict and count_dict[i] < 2:
                count_dict[i] = count_dict[i] + 1
            else:
                count_dict[i] = 1
        print(count_dict)
        for k, v in count_dict.items():
            if v == 1: return k
        return " "


if __name__ == '__main__':
    s = "aadadaad"
    res = Solution().firstUniqChar(s)
    print(res)

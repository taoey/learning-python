#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
核心思路：

判断两个单词是否包含重复字符可以化简为位运算 & 操作，当然也可以使用set来存储求交集，不过这样的话比较麻烦就是了
"""


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        wordsInt = [strToBit(i) for i in words]
        maxLen = 0
        for i in range(0, len(words)):
            for j in range(i, len(words)):
                if wordsInt[i] & wordsInt[j] == 0:
                    maxLen = max(maxLen, len(words[i])*len(words[j]))
        return maxLen


def strToBit(text):
    num = 0
    for s in text:
        num |= 1 << (ord(s)-97)
    return num


if __name__ == '__main__':
    s = Solution()
    words = ["abcw", "baz", "foo", "bar", "fxyz", "abcdef"]
    res = s.maxProduct(words=words)
    print(res)
    pass

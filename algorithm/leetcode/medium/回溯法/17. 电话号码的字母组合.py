#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 空值判断
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(index):
            # 出口遍历完毕
            if index == len(digits):
                res.append("".join(stack))
                return

            # 处理过程
            digit =digits[index] # 具体数字
            for item in phoneMap[digit]:  # 遍历具体数字代表的字符串
                stack.append(item)  # 放入当前位置的元素
                dfs(index+1)  # 放入下一个位置的元素
                stack.pop()
        res = []
        stack = []
        dfs(0)
        return res

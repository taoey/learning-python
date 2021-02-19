#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""
import re

"""
正则匹配 实际上是有限状态自动机  恶心人的题，跳过pass
"""

"""
恶心的用例： ".1" "e" ".e12" "."
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        # 去除正负号
        if re.match(r"[+|-]", s):
            s = s[1:]
        # 匹配科学计算
        match = re.match(r"\d+e([-|\d])\d+", s)
        if match and match.end() == len(s):
            return True
        # 匹配小数
        match = re.match(r"\d+\.\d+", s)
        if match and match.end() == len(s):
            return True
        # 匹配纯数字
        match = re.match(r"\d+", s)
        if match and match.end() == len(s):
            return True
        return False


if __name__ == '__main__':
    res = Solution().isNumber("e")
    print(res)
    s = ".1 "
    aa = re.match("\d+\.\d+", s)
    print(aa)

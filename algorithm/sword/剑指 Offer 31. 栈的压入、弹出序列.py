#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
"""

"""
解题思路：模拟栈的弹出
https://blog.csdn.net/weixin_43871956/article/details/107878378
"""

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, pop_index = [], 0
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return len(stack) == 0


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 1, 2]

    res = Solution().validateStackSequences(pushed, popped)
    print(res)

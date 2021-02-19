#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

利用dp思想，保存一个min数组，dp[i] = min(dp[i-1],i)
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_nums = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_nums) == 0:
            self.min_nums.append(x)
        else:
            self.min_nums.append(min(self.min_nums[-1], x))

    def pop(self) -> None:
        self.stack.pop()
        self.min_nums.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def min(self) -> int:
        if self.min_nums: return self.min_nums[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(1)
    param_3 = obj.top()
    param_4 = obj.min()
    print(param_3, param_4)

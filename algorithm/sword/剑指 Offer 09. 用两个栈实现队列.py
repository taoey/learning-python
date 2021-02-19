#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
"""


class CQueue:

    def __init__(self):
        self.headStack = []
        self.tailStack = []

    def appendTail(self, value: int) -> None:
        self.tailStack.append(value)

    def deleteHead(self) -> int:
        if self.headStack:
            return self.headStack.pop()
        elif self.tailStack:
            while self.tailStack:
                self.headStack.append(self.tailStack.pop())
            return self.headStack.pop()
        else:
            return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    item = arr.pop()
    print(item)

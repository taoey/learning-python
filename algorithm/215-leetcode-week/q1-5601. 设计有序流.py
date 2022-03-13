#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.arr = ["A" for i in range(n+1)]
        self.ptr = 1

    def insert(self, id: int, value: str) -> List[str]:
        res = []
        self.arr[id] = value
        if id < self.ptr:
            res = self.arr[id:self.ptr]
        else:
            for i in range(id, len(self.arr)):
                if self.arr[i] != "A":
                    res.append(self.arr[i])
                    self.ptr = i
                else:
                    break
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

if __name__ == '__main__':
    for i in range(1, 2):
        print(i)
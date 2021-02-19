#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 单独维护一个单调队列
import queue
from collections import deque


class MaxQueue:

    def __init__(self):
        self.common_queue = queue.Queue()
        self.max_queue = deque()
        self.index = 0

    def max_value(self) -> int:
        return self.max_queue[0][0] if self.max_queue else -1

    def push_back(self, value: int) -> None:
        self.index += 1
        self.common_queue.put((value, self.index))
        if self.common_queue.empty():
            self.common_queue.put((value, self.index))
            self.max_queue.append((value, self.index))
            return
        head = self.max_queue[0]
        if value >= head[0]:
            self.max_queue.clear()
            self.max_queue.append((value, self.index))
        else:
            tail = self.max_queue[len(self.max_queue) - 1]
            while value >= tail[0]:
                self.max_queue.pop()
                tail = self.max_queue[len(self.max_queue) - 1]
            self.max_queue.append((value, self.index))

    def pop_front(self) -> int:
        max_int = self.max_queue[0]
        head = self.common_queue.get()
        if head == max_int:
            self.max_queue.popleft()

        return head[0]


if __name__ == '__main__':
    s = MaxQueue()
    s.push_back(1)
    s.push_back(2)
    s.push_back(4)
    s.push_back(5)

    value = s.max_value()
    print(value)
    pass

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import queue

if __name__ == '__main__':
    q = queue.Queue()
    q.put(1)
    get = q.get()
    print(get)

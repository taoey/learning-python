#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
问题分析

复制链表比较费劲的是：random的存在

每个节点两处，多入
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        pass
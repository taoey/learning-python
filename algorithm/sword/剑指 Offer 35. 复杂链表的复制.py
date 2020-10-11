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

        n_dict = {}
        sentry_node = Node(0)
        cur, new_cur= head,sentry_node
        # 复制next指针
        while cur:
            new_node = Node(cur.val)
            new_cur.next = new_node
            n_dict[cur]= new_node

            cur,new_cur = cur.next,new_node

        # 复制random指针
        cur, new_cur = head, sentry_node.next
        while cur:
            if cur.random:
                new_cur.random = n_dict[cur.random]
            cur ,new_cur = cur.next,new_cur.next

        return sentry_node.next

if __name__ == '__main__':
    n = Node(0)
    print(n.val)
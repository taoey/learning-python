#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入两个链表，找出它们的第一个公共节点。

1、哈希表法    时间O(n+m) 空间O(n+m)
2、双指针遍历法  时间O(n+m) 空间O(1)
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a, cur_b = headA, headB
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA
        return cur_a

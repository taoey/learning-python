#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
low 的做法：遍历然后重组  空间O(n) 时间O(n)
进阶做法：中间点
"""


class Solution:
    def getMiddle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 暂存后继节点 cur.next
            cur.next = pre  # 修改 next 引用指向
            pre = cur  # pre 暂存 cur
            cur = tmp  # cur 访问下一节点
        return pre

    def reorderList(self, head: ListNode) -> None:
        if not head: return
        mid = self.getMiddle(head)
        mid_tmp = mid.next
        mid.next = None
        mid = mid_tmp

        left = head
        right = self.reverseList(mid)
        self.mergeList(left, right)

    def mergeList(self, left, right):
        while left and right:
            left_tmp = left.next
            right_tmp = right.next

            left.next = right
            left = left_tmp

            right.next = left
            right = right_tmp

    def toString(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res


def createList(arr):
    pass


if __name__ == '__main__':
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)  # mid
    e = ListNode(4)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    s = Solution()
    s.reorderList(a)
    res = s.toString(a)
    print(res)

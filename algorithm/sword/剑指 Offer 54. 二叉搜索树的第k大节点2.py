#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一棵二叉搜索树，请找出其中第k大的节点。

[5,3,6,2,4,null,null,1]
3
4
"""

"""
解题思路： 二叉搜索树左中右遍历为小中大，因此前序遍历右中左-->为大中小排列，利用递归，遍历k次后直接返回对应值即可
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            item = stack.pop()
            k -= 1
            if k == 0: return item.val
            cur = item.left

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.

"""
实际上就是二叉树的层序遍历
"""

import queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        dep = 0
        q = queue.Queue()
        q.put(root)
        while q.empty() is False:
            nodes_len = q.qsize()
            for i in range(nodes_len):
                node = q.get()
                if node.left: q.put(node.left)
                if node.right: q.put(node.right)
            dep += 1
        return dep


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c

    b.left = d
    c.right = e

    s = Solution()
    depth = s.maxDepth(a)
    print(depth)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def isSymLoop(left, right):
            # 都为空，有一个为空，都不为空
            if not left and not right: return True
            if not left or not right or left.val != right.val: return False
            return isSymLoop(left.left, right.right) and isSymLoop(left.right, right.left)

        return isSymLoop(root.left, root.right) if root else True

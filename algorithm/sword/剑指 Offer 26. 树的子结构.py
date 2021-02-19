# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 遍历A树
# 判断是否是子结构

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """判断B树是否A树的子结构"""
        result = False
        if A is not None and B is not None:
            if A.val == B.val:
                result = self.isSub(A, B)
            if result is False:
                result = self.isSubStructure(A.left, B)
            if result is False:
                result = self.isSubStructure(A.right, B)
        return result

    def isSub(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None: return True
        if A is None: return False
        if A.val != B.val: return False
        return self.isSub(A.left, B.left) and self.isSub(A.right, B.right)



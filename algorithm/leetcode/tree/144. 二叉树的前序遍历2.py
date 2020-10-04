#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack,result = [],[]


        return result

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)

    A.left = B
    A.right= C

    s = Solution()
    result = s.preorderTraversal(A)
    print(result)

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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result, stack = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            item = stack.pop()
            result.append(item.val)
            cur = item.right
        return result

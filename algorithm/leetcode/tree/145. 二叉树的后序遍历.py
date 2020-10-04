#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack, result = [root], []

        while stack:
            item = stack.pop()
            result.append(item.val)
            if item.left: stack.append(item.left)
            if item.right: stack.append(item.right)
        return result

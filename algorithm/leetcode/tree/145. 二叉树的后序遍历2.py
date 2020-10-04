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
        stack, result = [], []
        cur = root

        while stack or cur:
            while cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.right
            item = stack.pop()
            cur = item.left
        return result[::-1]

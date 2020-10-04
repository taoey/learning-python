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
        if not root: return []

        stack, result = [root], []

        while stack:
            item = stack.pop()
            result.append(item.val)
            # 入栈先右后左，保证出栈时的顺序为先左后右
            if item.right:
                stack.append(item.right)
            if item.left:
                stack.append(item.left)

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

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
import queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None : return []
        result = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            item = q.get()
            result.append(item.val)
            if item.left is not None: q.put(item.left)
            if item.right is not None: q.put(item.right)
        return result


if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)

    A.left = B
    A.right = C

    s = Solution()
    result = s.levelOrder(A)
    print(result)

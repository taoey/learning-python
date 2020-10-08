#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的广度优先遍历
import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        result = []
        q = queue.Queue()
        q.put(root)

        count = 1
        while not q.empty():
            tmp = []
            new_count = 0
            for _ in range(count):
                item = q.get()
                tmp.append(item.val)

                if item.left:
                    q.put(item.left)
                    new_count += 1
                if item.right:
                    q.put(item.right)
                    new_count += 1

            count = new_count
            result.append(tmp)
        return result
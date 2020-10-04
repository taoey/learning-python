#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
from typing import List
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的广度优先遍历
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
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


if __name__ == '__main__':
    A = TreeNode(1)

    B = TreeNode(2)
    C = TreeNode(3)

    D = TreeNode(4)
    E = TreeNode(5)

    A.left = B
    A.right = C

    B.left = D
    B.right = E

    s = Solution()
    result = s.levelOrder(A)
    print(result)

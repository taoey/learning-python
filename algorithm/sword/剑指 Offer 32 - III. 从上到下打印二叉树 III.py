#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import queue
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """之字形遍历"""
        if root is None : return []
        result = []
        q = queue.Queue()
        q.put(root)
        count = 1
        level = 1
        while not q.empty():
            new_count = 0
            tmp = []
            for _ in range(count):
                item = q.get()
                tmp.append(item.val)
                if item.left is not None :
                    q.put(item.left)
                    new_count+=1
                if item.right is not None :
                    q.put(item.right)
                    new_count+=1
            count = new_count
            if level % 2 !=0:
                result.append(tmp)
            else:
                result.append(tmp[::-1])
            level+=1
        return result

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)

    A.left = B
    A.right = C

    C.left = D
    C.right = E

    s = Solution()
    result = s.levelOrder(A)
    print(result)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树路径遍历变种

# 图的遍历：BFS/DFS

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root : return []
        result = []

        def dfs(root, path, ssum):
            mypath = copy.deepcopy(path)
            if not root.left and not root.right:
                if ssum+root.val == sum:
                    mypath.append(root.val)
                    result.append(mypath)
            else:
                mypath.append(root.val)
                ssum += root.val
                if root.left: dfs(root.left, mypath, ssum)
                if root.right: dfs(root.right, mypath, ssum)

        dfs(root, [], 0)
        return result

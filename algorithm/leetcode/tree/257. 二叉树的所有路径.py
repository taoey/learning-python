#!/usr/bin/env python
# -*- coding: utf-8 -*
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []

        def dfs(root, path):
            if root.left is None and root.right is None:  # 子节点
                path += str(root.val)
                result.append(path)

            else:
                path += str(root.val)+"->"
                if root.left:dfs(root.left,path)
                if root.right:dfs(root.right,path)

        if root:
            dfs(root, "")
        return result

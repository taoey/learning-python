#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
二叉搜索树的特点是：左子树 < root < 右子树
后序遍历时采用的是：左 右 root , 故可利用递归，看左子树和右子树是否符合搜索树顺序。
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
"""


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            cur = i
            while postorder[cur] < postorder[j]: cur += 1  # 划分左子树：[i:cur]
            left = cur

            while postorder[cur] > postorder[j]: cur += 1  # 划分右子树 [left:cur]
            return cur == j and recur(i, left-1) and recur(left, j-1)

        return recur(0, len(postorder) - 1)


if __name__ == '__main__':
    print()

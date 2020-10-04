#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        stack, result = [root], []

        while stack:
            item = stack.pop()
            result.append(item.val)
            if item.children: stack.extend(item.children[::-1])

        return result


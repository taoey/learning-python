#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
请实现两个函数，分别用来序列化和反序列化二叉树。
    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
"""

# Definition for a binary tree node.
import collections
from queue import Queue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        二叉树层序遍历
        :param root:
        :return:
        """
        if not root: return "[]"
        res = []
        q = Queue()
        q.put(root)
        while not q.empty():
            cur = q.get()
            if cur:
                res.append(str(cur.val))
                # 存放下一层节点 none节点也需要存放
                q.put(cur.left)
                q.put(cur.right)
            else:
                res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root



if __name__ == '__main__':
    a = TreeNode(1)

    b = TreeNode(2)
    c = TreeNode(3)

    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c

    c.left = d
    c.right = e

    res = Codec().serialize(a)
    print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -- BEGIN --
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left)
            # 处理中间root节点
            if self.pre:
                self.pre.right = cur
                cur.left = self.pre
            else:
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root: return
        self.pre = None
        dfs(root)
        # 遍历拼接完毕，构建首尾连接，self.pre为最后一个遍历的节点，
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
# -- END --

def list2arr(root):
    result = []
    my_set = set()
    cur = root
    while cur and cur not in my_set:
        my_set.add(cur)
        result.append(cur.val)
        cur = cur.right
    return result


if __name__ == '__main__':
    a = Node(4)
    b = Node(2)
    c = Node(5)
    d = Node(1)
    e = Node(3)

    a.left = b
    a.right = c

    b.left = d
    b.right = e
    res = Solution().treeToDoublyList(a)
    print(list2arr(res))
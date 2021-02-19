# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#
#
#
#  示例 1:
#
#  给定二叉树 [3,9,20,null,null,15,7]
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回 true 。
#
# 示例 2:
#
#  给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#         1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
#  返回 false 。
#
#
#
#  限制：
#
#
#  1 <= 树的结点个数 <= 10000
#
#
#  注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
#
#
#  Related Topics 树 深度优先搜索
#  👍 101 👎 0

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(cur):
            # 获取当前节点的左右子树高度
            left_dep, right_dep = self.maxDepth(cur.left), self.maxDepth(cur.right)
            # 判断左子树是否平衡
            left_res = dfs(cur.left) if cur.left else True
            # 判断右子树是否平衡
            right_res = dfs(cur.right) if cur.right else True
            return abs(left_dep - right_dep) <= 1 and left_res and right_res  # 当前子树平衡并且左右子树平衡

        if not root: return True
        return dfs(root)

    def maxDepth(self, root):
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(1)
    c = TreeNode(1)
    d = TreeNode(1)
    e = TreeNode(1)

    # a.left = b
    a.right = c

    c.left = d
    # c.right = e

    res = Solution().isBalanced(a)
    print(res)

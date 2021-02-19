# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？ 
# 
#  
# 
#  示例 1: 
# 
#  输入: 
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物 
# 
#  
# 
#  提示： 
# 
#  
#  0 < grid.length <= 200 
#  0 < grid[0].length <= 200 
#  
#  Related Topics 动态规划 
#  👍 91 👎 0

"""
状态转移方程： dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + grid[i][j]
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        dp = [[1] * len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]  # top边界
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]  # left边界
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[-1][-1]


# leetcode submit region end(Prohibit modification and deletion)

"""
第一次失败用例：[[0]] 测试结果:1 期望结果:0
第二次失败用例：[[1,2,5],[3,2,1]] 
"""

if __name__ == '__main__':
    arr = [[1, 2, 5], [3, 2, 1]]
    res = Solution().maxValue(arr)
    print(res)

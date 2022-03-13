#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        arr = [[0] * (len(text1)+1) for _ in range(len(text2)+1)]
        # 建立二维数组
        # 使用这种二维数组初始化坑死我了
        # arr_in = [0] * (len(text1) + 1)
        # arr = [arr_in for i in range(len(text2) + 1)]
        arr = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]
        # 遍历二维数组
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    arr[i][j] = arr[i - 1][j - 1] + 1
                else:
                    arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
        # 返回最终值
        return arr[-1][-1]


if __name__ == '__main__':
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"
    res = Solution().longestCommonSubsequence(text1, text2)
    print(res)  # 1

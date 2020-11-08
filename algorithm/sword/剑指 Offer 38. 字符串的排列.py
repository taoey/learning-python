#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(index, path):
            """
            :param index:  当前遍历的层级
            :param path: 处理过程中的字符串
            :return:
            """
            # 定义出口
            if index == len(s):
                res.append("".join(path))

            # 处理过程
            show_set = set() # 对于已经出现过的不再做处理
            for i in range(index, len(s)):
                if path[i] in show_set: continue
                show_set.add(path[i])

                path[index],path[i] = path[i],path[index]
                dfs(index+1, path)
                path[index], path[i] = path[i], path[index]

        res = []
        dfs(0, list(s))
        return res


if __name__ == '__main__':
    s = Solution()
    mystr = 'abb'
    res = s.permutation(mystr)
    print(res)

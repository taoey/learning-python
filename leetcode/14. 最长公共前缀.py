#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or  len(strs) == 0 :return ""
        end_flag = False
        head = strs[0]
        index = 0
        for i in range(len(head)):
            for j in range(len(strs)):
                cur = strs[j]
                if i >= len(cur) or cur[i] != head[i]:
                    end_flag = True
                    break
            if end_flag is True:
                return head[0:i]
        return head




if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    s = Solution()
    prefix = s.longestCommonPrefix(strs)
    print(prefix)
    # aa= "123"
    # print(aa[0:2])

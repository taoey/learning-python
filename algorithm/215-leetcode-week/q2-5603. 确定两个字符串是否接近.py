#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

# 根据题目，可以看出，相似字符串符合规律：两个字符串中字符种类相同,字符出现的次数排列后一致，

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 统计每个字符出现次数
        counter1 , counter2 = collections.Counter(word1), collections.Counter(word2)

        # 对比统计后的键和值
        if set(word1) == set(word2):
            v1, v2 = counter1.values(), counter2.values()
            if sorted(v1) == sorted(v2):
                return True
        return False



if __name__ == '__main__':
    mystr = "taoeyaa"
    counter = collections.Counter(mystr)
    print(counter.keys())

    print(set(counter.keys()))

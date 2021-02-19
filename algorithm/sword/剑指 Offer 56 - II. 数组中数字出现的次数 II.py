#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

"""
判断位运算之和
&	与	    两个位都为1时，结果才为1
|	或	    两个位都为0时，结果才为0
^	异或	    两个位相同为0，相异为1
~	取反  	0变1，1变0
<<	左移	    各二进位全部左移若干位，高位丢弃，低位补0
>>	右移	    各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移）
"""


"""
需要掌握的点：
- 如何获取某数二进制第n位的值
- 通过或操作将某一位置为1
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            cur_sum = 0  # 当前位之和
            idx = 1 << i
            for num in nums:
                if num & idx != 0:
                    cur_sum += 1
            if cur_sum % 3 == 1:
                res |= idx
        return res


if __name__ == '__main__':
    x = bin(pow(2, 32)).replace('0b', '')
    pass

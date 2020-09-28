#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
参考资料：
http://sshpark.com.cn/2018/11/22/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%EF%BC%9A%E8%B4%A5%E8%80%85%E6%A0%91/
https://www.it610.com/article/1305779568971386880.htm
"""

K = 4  # 4路归并
buf = []  # 存放多路归并的头元素，多出来的一位放最小值
ls = []  # ls[0]保存的是胜者的下标，其余保存败者下标号


def adjust(s):
    """定义调整函数 s是buf数组的下标"""
    t = (s + K) // 2  # 取s位的父节点

    # 如果当前节点不是根节点则进入下次循环，否则跳出
    while t > 0:
        # 比较当前节点值与父节点对应的值，如果父节点胜出则记录失败者并将当前节点换成胜利者
        if buf[s] > buf[ls[t]]:
            l = ls[t]
            ls[t] = s
            s = l
        t = t // 2
    # 记录最终胜利者到ls[0]
    ls[0] = s


def build():
    """定义败者树构建函数"""
    # 添加最小值-1到buf尾部
    buf.append(-1)

    # 将败者树中间节点全部初始化为最小值所在位置即len(buf)-1
    for i in range(len(buf)):
        ls.append(len(buf) - 1)

    # 依次调整buf列表中所有位置
    for i in range(K):
        adjust(i)

def get_min():
    return buf[ls[0]]

if __name__ == '__main__':
    myarr = [12, 7, 6, 8]
    buf = myarr
    build()

    print(get_min())
    buf[2] = 1
    adjust(2)
    print(get_min())
    pass

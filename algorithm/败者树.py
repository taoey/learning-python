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
MIN = -1  # 最小值要取对，保存在全部数中为最小


def adjust(index):
    """定义调整函数 s是buf数组的下标"""
    f_index = (index + K) // 2  # 取index的父节点
    print("f_index:",f_index)

    # 如果当前节点不是根节点则进入下次循环，否则跳出
    while f_index > 0:
        # 比较当前节点值与父节点对应的值，如果父节点胜出则记录失败者并将当前节点换成胜利者(当前规则：大者为败，小者为胜)
        if buf[index] > buf[ls[f_index]]:
            l = ls[f_index]
            ls[f_index] = index
            index = l
        f_index = f_index // 2
    # 记录最终胜利者到ls[0]
    ls[0] = index
    print(buf,ls)


def build():
    """定义败者树构建函数"""
    # 添加最小值-1到buf尾部
    buf.append(MIN)

    # 将败者树中间节点全部初始化为最小值所在位置即len(buf)-1
    for i in range(len(buf)):
        ls.append(len(buf) - 1)

    # 依次调整buf列表中所有位置
    for i in range(K):
        adjust(i)


def get_min():
    return buf[ls[0]]


if __name__ == '__main__':
    buf = [12, 10, 6, 8]
    build()

    print(get_min())
    buf[2] = -3
    adjust(2)
    print(get_min())
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print_msg是外围函数
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer


if __name__ == '__main__':
    # 这里获得的就是一个闭包
    closure = print_msg()
    # 输出 I'm closure
    closure()

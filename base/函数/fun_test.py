#!/usr/bin/env python
# -*- coding: utf-8 -*-


def aa(num):
    print('aa', num)


def bb(num):
    print('bb', num)


def cc(num):
    print('cc', num)


fun_dict = {
    'AA': aa,
    'bb': bb,
    'cc': cc
}

if __name__ == '__main__':
    fun_name = "aa"
    fun_name = fun_name.upper()
    print(fun_name)
    if fun_name in fun_dict:
        fun = fun_dict[fun_name](13)
    print('run over...')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s()' % func.__name__)
        print('args = {}'.format(*args))
        print(kwargs)
        return func(*args, kwargs)

    return wrapper


@log
def mytest(p, aa):
    print(mytest.__name__ + " param: " + p)


if __name__ == '__main__':
    mytest("I'm a param", aa=10)

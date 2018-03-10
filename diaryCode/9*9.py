#!/usr/bin/env python3
#coding:utf-8


if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d*%d =%d" % (j,i,j*i),end=" ")
        print("\n")
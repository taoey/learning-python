#!/usr/bin/env python3
#coding:utf-8
import math


def isPrimeNum(num):
    if num==1:
        return False
    else:
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True

def sumPrime(num1,num2):
    sum = 0
    for i in range(num1,num2):
        if isPrimeNum(i):
            sum = sum + i
    return sum

if __name__ == '__main__':
    data = sumPrime(1,100)
    print(data)
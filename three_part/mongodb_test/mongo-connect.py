#!/usr/bin/env python3
#coding:utf-8

from pymongo import MongoClient


if __name__ == '__main__':
    client=MongoClient()
    db=client.Taoey
    collection=db['80sMovies']
    datas=collection.find()[0:1]
    count=0
    for i in datas:
        count=count+1
        print(i)
    print(count)

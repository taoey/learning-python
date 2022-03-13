#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from datetime import datetime
import datetime
import pytest

def test_01():
    mytime = datetime.now().strftime('%Y-%m-%d')
    start_time = mytime + " 00:00:00"
    end_time = mytime + " 23:59:59"
    print("tao", mytime, start_time, end_time)

    table = "vip_order"
    sql = 'select distinct(ktv_id) from {} where state in (2, 8) and finish_time>="{}" and  finish_time<="{}"'.format(table, start_time, end_time)
    print(sql)


def test_02():
    str_p = '2019-01-30'
    dateTime_p = datetime.datetime.strptime(str_p, '%Y-%m-%d')
    print(dateTime_p)  # 2019-01-30 15:29:08


def test_03():
    str_p = '2019-01-30'
    today = datetime.datetime.strptime(str_p, '%Y-%m-%d')
    tomorow = today + datetime.timedelta(days=1)

    tomorow_p = datetime.datetime.strftime(tomorow, '%Y-%m-%d')
    print(today, tomorow, tomorow_p, type(tomorow), type(tomorow_p), max(today, tomorow))

    if tomorow > today:
        print("yess")

    next = datetime.datetime.strptime("2019-01-31", '%Y-%m-%d')
    if tomorow == next:
        print("yes")

def test_04():
    """字符串转为时间戳,然后判断和当前时间的时间差（秒）"""
    str_p = '2020-12-04 15:24:28'
    tp = datetime.datetime.strptime(str_p, '%Y-%m-%d %H:%M:%S').timetuple()
    ttl = int(time.time()) - int(time.mktime(tp))
    print(ttl)

def test_05():
    mytime = datetime.datetime.now().strftime('%Y%m%d')
    print(mytime)


def test_06():
    str_p = '2019-01-30'
    pre = datetime.datetime.strptime(str_p, '%Y-%m-%d')

    now = datetime.datetime.now()
    print(pre > now)
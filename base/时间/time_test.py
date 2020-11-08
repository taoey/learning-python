#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import datetime
import pytest

def test_01():
    mytime = datetime.now().strftime('%Y-%m-%d')
    start_time = mytime+" 00:00:00"
    end_time = mytime+" 23:59:59"
    print("tao",mytime,start_time,end_time)

    table = "vip_order"
    sql = 'select distinct(ktv_id) from {} where state in (2, 8) and finish_time>="{}" and  finish_time<="{}"'.format(table,start_time,end_time)
    print(sql)

def test_02():
    str_p = '2019-01-30'
    dateTime_p = datetime.datetime.strptime(str_p, '%Y-%m-%d')
    print(dateTime_p)  # 2019-01-30 15:29:08


def test_03():
    str_p = '2019-01-30'
    today = datetime.datetime.strptime(str_p, '%Y-%m-%d')
    tomorow = today +  datetime.timedelta(days=1)

    tomorow_p = datetime.datetime.strftime(tomorow, '%Y-%m-%d')
    print(today,tomorow ,tomorow_p,type(tomorow),type(tomorow_p))

    next = datetime.datetime.strptime("2019-01-31", '%Y-%m-%d')
    if tomorow == next:
        print("yes")

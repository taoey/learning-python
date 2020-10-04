#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

import pytest

def test_01():
    mytime = datetime.now().strftime('%Y-%m-%d')
    start_time = mytime+" 00:00:00"
    end_time = mytime+" 23:59:59"
    print("tao",mytime,start_time,end_time)

    table = "vip_order"
    sql = 'select distinct(ktv_id) from {} where state in (2, 8) and finish_time>="{}" and  finish_time<="{}"'.format(table,start_time,end_time)
    print(sql)

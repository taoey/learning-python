#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

if __name__ == '__main__':
    dt = "2020-09-30"
    dt = datetime.strptime(dt, '%Y-%m-%d').date() if dt else datetime.now().date()
    d5 = (dt.strftime('%Y%m%d'), (dt - timedelta(1)).strftime('%Y%m%d'), (dt - timedelta(7)).strftime('%Y%m%d'),
          (dt - timedelta(14)).strftime('%Y%m%d'), (dt - timedelta(21)).strftime('%Y%m%d'))
    print(d5)

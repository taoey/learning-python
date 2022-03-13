#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)


def test_01():
    zrange = client.zrangebyscore("paying_orders", 0, 1606724870, 0, 2)
    print(type(zrange), zrange)  # redis_zset_mq.py .<class 'list'> [b'orderid0001', b'orderid0002']
    if zrange:
        orderids = [i.decode() for i in zrange]
        print(orderids)


def test_02():
    zrange = client.zrangebyscore("paying_orders", 0, 1606724870, 0, 2, withscores=True,)
    print(type(zrange), zrange) # redis_zset_mq.py .<class 'list'> [(b'orderid0001', 1606723465.0), (b'orderid0002', 1606723466.0)]
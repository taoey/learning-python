#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)


def mysql_close_orders(orderids):
    # TODO： Mysql批量关闭orderids个订单
    sql_1 = """
    UPDATE book_order
             SET status = CASE id
                 WHEN 1001 THEN 2
                 WHEN 1002 THEN 2
                 WHEN 1003 THEN 2
             END
    WHERE id IN (1001,1002,1003)
    """

    sql_2 = """UPDATE user SET status=1 WHERE id in ('1001,1002,1003');"""
    print(orderids)
    pass


def zrangebyscore_and_rem(key, min, max, limit):
    zrangebyscore_and_rem_str = """
        local message = redis.call('ZRANGEBYSCORE', KEYS[1], ARGV[1], ARGV[2], 'LIMIT', 0, ARGV[3]);
        if #message > 0 then
            for i = 1, #message do 
                redis.call('ZREM', KEYS[1], message[i]);
            end 
            return message;
        else
            return {};
        end
    """
    zrangebyscore_and_rem_lua = client.register_script(zrangebyscore_and_rem_str)
    res = zrangebyscore_and_rem_lua(keys=[key], args=[min, max, limit])
    return [i.decode() for i in res]


def get_change_orders(time_min, time_max, limit):
    return zrangebyscore_and_rem("paying_orders", time_min, time_max, limit)


if __name__ == '__main__':
    try:
        # 当前秒级时间戳
        interval = 60
        time_second_now = int(time.time())
        time_second_ago = time_second_now - interval
        # limit：每次需要处理的任务数量，可以根据需要配置成可传入参数
        limit = 1000

        orderids = get_change_orders(time_second_ago, time_second_now, limit)
        if orderids:
            mysql_close_orders(orderids)
    except Exception as e:
        print(e)


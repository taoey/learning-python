#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

client = redis.StrictRedis(host="127.0.0.1", port=6379)

#             redis.call('ZREMRANGEBYSCORE', KEYS[1], ARGV[1], ARGV[2]);
if __name__ == '__main__':
    zrangebyscore_and_rem = """
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
    zrangebyscore_and_rem_lua = client.register_script(zrangebyscore_and_rem)
    res = zrangebyscore_and_rem_lua(keys=["paying_orders"], args=[0, int(time.time()), 1])
    print(res)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import consul

if __name__ == '__main__':
    c = consul.Consul(host='192.168.3.130', port=8500, scheme='http')
    data = c.kv.get("tao")
    print(data)

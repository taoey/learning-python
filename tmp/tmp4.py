#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

if __name__ == '__main__':
    params = {
        "mchId": "399210203068121",
        "billDate": "2021-03-03",
        "billType": 1,
    }
    url = "&".join(['%s=%s' % (str(key), str(params[key])) for key in sorted(params) if params[key]])
    sign = hashlib.md5(url.encode('utf8')).hexdigest().upper()
    print(sign)

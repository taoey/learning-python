#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


if __name__ == '__main__':
    url = "https://www.vmgirls.com/wp-admin/admin-ajax.php"

    payload = {'append': 'list-archive',
               'paged': '2',
               'action': 'ajax_load_posts',
               'query': '少女',
               'page': 'tag'}
    headers = {
        "User-Agent": "PostmanRuntime/7.26.8",
        "Cache-Control":"no-cache",
        "Content-Type":"multipart/form-data; boundary=<calculated when request is sent>",
        "Accept":"*/*",
        "Connection": "keep-alive"
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.content.decode())

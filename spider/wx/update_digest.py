#!/usr/bin/env python
# -*- coding: utf-8 -*-
from spider.wx.mysql import get_item_by_id, update

if __name__ == '__main__':
    for i in range(2625):
        cur_id = i
        item = get_item_by_id(cur_id)
        digest = item.get("digest", "")
        index = digest.find("猫猫推荐")
        if index != -1:
            update(cur_id, digest=digest[0:index])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime

from mako.template import Template

from spider.wx.mysql import get_muti_unupload

if __name__ == '__main__':
    dir = "mds/"
    muti = get_muti_unupload(50, 58)
    today = datetime.now().strftime("%Y-%m-%d")
    for item in muti:
        if item["pic_url"]: item["pic_url"] = json.loads(item["pic_url"])
        pic_url = item["pic_url"]["pics"]
        item["emoji"] = pic_url[-1]
        item["pic_url"] = pic_url[:-1]
    print(muti)
    mytemplate = Template(filename='today_html.template')
    body = mytemplate.render(title=today, muti=muti)
    with open(dir + today + ".html", "w", encoding='utf-8') as f:
        f.write(body)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
xlwt 只能创建xls的文件 不支持xlsx文件，但是这个库比较好安装 （推荐使用，如果想要获得xlsx文件，可以通过excel的文件另存为获取）

openpyxl 不好安装，只能通过源码安装



参考资料：
- https://www.cnblogs.com/wanglle/p/11455758.html
- https://www.cnblogs.com/paul-liang/p/9187503.html
- https://www.cnblogs.com/lalalatianlalu/p/10387289.html
"""
import xlwt
from datetime import datetime

if __name__ == '__main__':


    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    ws.write(0, 0, 1234.56, style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, "hello world")
    ws.write(3, 0, 1)
    ws.write(3, 1, 3)
    ws.write(3, 2, xlwt.Formula("A4+B4"))
    wb.save('example.xls')

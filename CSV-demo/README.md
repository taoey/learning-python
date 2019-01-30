## python操作csv文件

需要读取操作的文件:test_data.csv
```csv
'name','age'
'tao','12'
'hong','13'
'明','15'
```

第一次读测试:
```python
#encoding:utf-8
import csv

if __name__ == '__main__':
    csv_file = csv.reader(open('test_data.csv','r'))
    for line in csv_file:
        print(line)
```
**测试结果**
```
D:\Anaconda\python.exe E:/projects/python/python_deoms/CSV-demo/CSV_Demo.py
Traceback (most recent call last):
  File "E:/projects/python/python_deoms/CSV-demo/CSV_Demo.py", line 6, in <module>
    for line in csv_file:
UnicodeDecodeError: 'gbk' codec can't decode byte 0x8e in position 42: illegal multibyte sequence
```
我们可以看到主要的报错信息是编码错误，我们只需要解决的编码问题即可，详见第二次测试


第二次读测试：
添加了codes模块
```python
#encoding:utf-8
import csv
import codecs

if __name__ == '__main__':
    csv_file = csv.reader(codecs.open('test_data.csv','r','utf-8'))
    for line in csv_file:
        print(line)

```
**测试结果**

```
D:\Anaconda\python.exe E:/projects/python/python_deoms/CSV-demo/CSV_Demo.py
["'name'", "'age'"]
["'tao'", "'12'"]
["'hong'", "'13'"]
["'明'", "'15'"]
```
根据结果，我们看到，我们成功读出了csv中的内容
## python 脚本小工具

### shell-CSV2SQL.py
由csv拼接完整SQL的脚本工具

使用说明：csv文件必须和脚本在同一路径下
输入的SQL解释：
```
update student set age = '{1}',name = '{0}';
```
其中的数字代表的是csv文件中数据的位置，示例csv文件如下：
```
tao,12
hong,13
明,15
```
生成的sql文件内容：
```
update student set age = '12',name = 'tao';
update student set age = '13',name = 'hong';
update student set age = '15',name = '明';
```

**注意：**
如果需要重新生成，需要把之前的生成的文件删除掉
"""
对应博客:
"""
import json


## dic数据转化为json对象
dicData={
    "name":"黄为涛",
    "sex": "male",
    "school":["a","b","c"]
}

#jsonObj=json.dumps(dicData)
jsonObj=json.dumps(dicData,ensure_ascii=False)
print(type(jsonObj),jsonObj)

## json数据转化为dic数据,以获取其中的具体信息

## 载入数据乱码问题

## 处理从网页获取的json数据


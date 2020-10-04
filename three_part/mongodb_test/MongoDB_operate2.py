#coding=utf-8
from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        client = MongoClient()
        self.db=client.Taoey

    def insert(self,data,dataArrt=None):
        '''
        增加一条数据,如果没有约束项dataArrt则直接插入
        :param data: 要插入的数据项,要求是字典
        :param dataArrt: 要插入数据项的主键属性
        '''
        if dataArrt==None:
            self.db.Test.insert_one(data)
        else:
            r=self.db.Test.find(dataArrt)
            if r.count()==0:
                self.db.Test.insert_one(data)
                print("插入成功")
            else:
                print("数据已存在")
                pass

    def remove(self,data=None):
       '''删除一条数据,传入一个字典数据
       1.
        id = db.Test.find_one({'_name':'我的小说'})['_id']
        db.Test.remove(id) # 根据 id 删除一条记录
       2.
        db.Test.remove() # 删除集合里的所有记录
       3.
        db.Test.remove({'yy':5}) # 删除yy=5的记录
       '''
       if data==None:
           self.db.Test.remove()
       else:
           self.db.Test.remove(data)

    def update(self,who,newData):
        '''

        db.users.update({“name”:“user1”}, {“$set”:{“age”:100, “sex”:0}}) # update users set age = 100, sex = 0 where name = 'user1'

        db.users.update({}, {“$inc”:{“age”:10}}, multi=True) # update users set age = age + 10

        db.users.update({“name”:“user1”}, {“$inc”:{“age”:10}, “$set”:{“sex”:1}}) # update users set age = age + 10, sex = 1 where name = 'user1'


        '''
        self.db.Test.update(who,data)

    def find(self,data1=None,data2=None):
        '''
        模拟数据库中的查找操作
        :param data1:查询操作的第一个数据
        :param data2:查询操作的第二个数据
        :return:
        '''
        if data2==None:
            return self.db.Test.find(data1)
        elif data1==None:
            return self.db.Test.find()
        else:
            return self.db.Test.find(data1,data2)

    def isEmpty(self,data=None):
        '''
        判断查询结果是否为空,如果不传入数据,则默认查询整个数据库
        :param data: 传入一个Cursor游标对象
        '''
        if data==None:
            r=self.db.Test.find()
            if r.count()==0:
                return True
            else:
                return False
        else:
            if data.count()==0:
                return True
            else:
                return False


if __name__ == '__main__':
    # 操作的数据
    book1 = {
        '_name': "数据结构和算法",
        '_price': 42,
        '_writer': {
            "_Name": "大神",
            '_Age': 36,
            '_Sex': "man",
            '_From': 'China',
        },
    }
    book2 = {
        '_name': "我的小说",
        '_price': 10,
        '_writer': {
            "_Name": "me",
            '_Age': 22,
            '_Sex': "man",
            '_From': 'China',
        },
    }
    book3 = {
        '_name': "天书",
        '_price': 100,
        '_writer': {
            "_Name": "God",
            '_Age': 100,
            '_Sex': "man",
            '_From': 'none',
        },
    }

    db=MongoDB()

    db.insert(book1,{"_name":book1["_name"]})

    r1=db.find({"_name":"数据结构和算法"})

    print(r1.count())

    for i in r1:
        print(i["_name"])

    #db.remove()
    print(db.isEmpty())



import pymysql

def get_connect():
    """
    创建连接
    :return:
    """
    host = '123.207.155.241'
    user = 'root'
    password = 'CTn2IgDt3hgi'
    database = 'ju_friends'
    return pymysql.connect(host, user, password, database)

def insert(file_name,key_name):
    db = get_connect()
    cursor = db.cursor()
    # 获取敏感数据并插入
    with open(file_name, "r+", encoding='utf-8') as f:
        for line in f.readlines():
            word = line.strip()
            sql = "INSERT INTO `sys_dic`(`status`,pid,`key`,`value`) VALUE({},{},'{}','{}')".format(1, 1,key_name, word)
            print(sql)
            cursor.execute(sql)
    db.close()

if __name__ == '__main__':
    files = ['网址.txt','广告.txt','政治.txt','色情.txt','其他.txt']
    key_names =['网址','广告','政治','色情','其他']
    for i in range(0,len(files)):
        insert(files[i],key_names[i])
    pass
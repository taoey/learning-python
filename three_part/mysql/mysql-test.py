import pymysql


def get_connect():
    """
    创建连接
    :return:
    """
    host = '123.207.155.241'
    user = 'root'
    password = 'CTn2IgDt3hgi'
    database = 'test'
    return pymysql.connect(host, user, password, database)

def select(sql):
    """
    查询语句执行模板
    :param sql:
    :return:
    """
    db = get_connect()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result


if __name__ == '__main__':
    select_sql = 'select * from student'
    results = select(select_sql)
    print(results)
    pass

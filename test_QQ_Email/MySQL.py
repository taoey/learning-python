import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="test", charset="utf8")

cur = conn.cursor()

sql = "select * from books"

cur.execute(sql)

rows = cur.fetchall()

# print(rows)

for dr in rows:
    print(dr)
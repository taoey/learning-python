import csv
import codecs

if __name__ == '__main__':
    filename = input("请输入csv文件名称：")
    sql = input("请输入SQL语句，例如：update student set age = '{1}',name = '{0}';:")

    file_csv = csv.reader(codecs.open(filename, 'r', 'utf-8'))
    file_writer = codecs.open('file_out.txt', 'a', 'utf-8')

    count = 0
    for line in file_csv:
        out_sql = sql.format(*line)
        file_writer.write(out_sql+"\n")
        print("写入：{}成功".format(out_sql))
        count = count + 1
    print("写入完成，共{}条数据".format(count))
    file_writer.close()
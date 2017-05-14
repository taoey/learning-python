'''
测试成功

打开文件,并替换其中的全部字符
'''

def file(path,old,new):
    with open(path, "r+",encoding='utf-8') as f:  # 不用w w会清空数据
        s = f.read()  # 读出
        f.seek(0, 0)  # 指针移到头
        f.flush()
        f.write(s.replace(old, new))
        f.close()

if __name__ == '__main__':
    file("data.txt","Hello","你好")
    file("data.txt", "World", "世界")

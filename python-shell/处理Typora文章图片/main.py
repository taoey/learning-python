import re
from qiniu import Auth, put_file, PersistentFop, build_op, op_save, urlsafe_base64_encode


def upload_img(file_name, file_path):
    access_key = ""
    secret_key = ""

    q = Auth(access_key, secret_key)
    bucket_name = 'python_wx_pic'
    key = file_name
    token = q.upload_token(bucket_name, key, 3600)
    localfile = file_path
    ret, info = put_file(token, key, localfile)
    print(file_name,"上传成功")

    return ret["key"]

if __name__ == '__main__':

    file_name = input("请输入文件路径：")
    file_save_name = input("保存为：")
    file_name_search = re.search(r'(.*)\\.*', file_name)
    file_save_path = file_name_search.group(1) + "\\" + file_save_name
    #匹配所有本地图片
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 处理图片格式内容
            search = re.search(r'!\[.*\]\(((.*)\.assets/(.*)\.(.*))\)', line, re.I)
            if search != None:
                # 上传匹配到的图片
                # print(search.group())
                # print(search.group(1))
                # print(search.group(2))
                # print(search.group(3))

                pic_path = file_name_search.group(1)+'\\'+search.group(1)
                pic_name = search.group(2)+search.group(3)+"."+search.group(4)

                key = upload_img(pic_name, pic_path)
                # key 之后的一长串是水印代码
                pic_url = "http://pqkft7tpa.bkt.clouddn.com/"+key\
                          +"?imageView2/0/q/100|watermark/2/text/44CQ5b6u5L-h5YWs5LyX5Y-377ya5Z2C5pys5YWI55Sf44CR/font/6buR5L2T/fontsize/400/fill/IzNGOTREQQ==/dissolve/100/gravity/NorthEast/dx/10/dy/10"


                line = line.replace(search.group(1), pic_url)
                with open(file_save_path, "a", encoding="utf-8") as write_file:
                    write_file.write(line)
            else:
                with open(file_save_path, "a", encoding="utf-8") as write_file:
                    write_file.write(line)
    f.close()
    print("转化完成")

import re
from qiniu import Auth, put_file, PersistentFop, build_op, op_save, urlsafe_base64_encode

config = {
    access_key: "",
    secret_key: "",
    os: "unix",  # unix/win
    bucket_name: "python_wx_pic",
    domain: "http://qiniuimg.beangogo.cn"  # 例如：http://qiniuimg.beangogo.cn
}


def upload_img(file_name, file_path):
    access_key = config["access_key"]
    secret_key = config["secret_key"]

    q = Auth(access_key, secret_key)
    bucket_name = config["bucket_name"]
    key = file_name
    token = q.upload_token(bucket_name, key, 3600)
    localfile = file_path
    ret, info = put_file(token, key, localfile)
    print(file_name, "上传成功")

    return ret["key"]


if __name__ == '__main__':

    file_name = input("请输入文件路径：")
    file_save_name = input("保存为：")
    file_name_search = re.search(r'(.*)/.*', file_name)
    file_save_path = file_name_search.group(1) + "/" + file_save_name
    print(file_save_path)
    # 匹配所有本地图片
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f.readlines():
            # 处理图片格式内容
            search = re.search(r'!\[.*\]\(((.*)\.assets/(.*)\.(.*))\)', line, re.I)
            if search != None:
                # 上传匹配到的图片
                pic_path = file_name_search.group(1) + '/' + search.group(1)
                pic_name = search.group(2) + "-" + search.group(3) + "." + search.group(4)

                key = upload_img(pic_name, pic_path)

                pic_url = config["domain"] + "/" + key

                line = line.replace(search.group(1), pic_url)
                with open(file_save_path, "a", encoding="utf-8") as write_file:
                    write_file.write(line)
            else:
                with open(file_save_path, "a", encoding="utf-8") as write_file:
                    write_file.write(line)
    f.close()
    print("转化完成")

import os
import shutil


def copy_pictures():
    """
    备份图片，处理单个文件时从备份文件中获取图片
    :return:
    """
    shutil.copytree("assets", "assets_copy")
    pass


def resolve_one_file(file_path):
    """
    处理单个文件
    :return:
    """
    with open(file_path, 'r', encoding="utf-8") as f :
        for line in f:
            print(line)
    pass


if __name__ == '__main__':

    dir = "E:\\temp\\MyNote\\我的精品博文系列\\"
    for file in os.listdir(dir):
        if file != "assets":
            print("处理文件：{}".format(file))
            resolve_one_file(dir+file)
    pass


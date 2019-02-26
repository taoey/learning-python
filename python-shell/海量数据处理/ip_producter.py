import random
import time

def ip_producter(num):
    """
    海量IP生成器，至少需要产出1000个IP
    :param num: 需要产生的IP数量
    :return:
    """
    random_max = num/200
    with open('data.txt', 'a', encoding='utf-8') as f:
        for i in range(0, num):
            ip = '{}.{}.{}.{}'.format(random.randint(1, 128), random.randint(0, 128),
                                      random.randint(0, 128), random.randint(0, 128))
            # 构造重复IP
            if i % 1000 == 0:
                for _ in range(0, random.randint(1, random_max)):
                    f.write('{}\n'.format(ip))
            else:
                f.write('{}\n'.format(ip))
        f.close()


if __name__ == '__main__':
    num = int(input('请输入需要产生的IP数量，例如1000：'))
    start = int(round(time.time() * 1000))
    try:
        ip_producter(num)
        end = int(round(time.time() * 1000))
        print('IP产生结束，用时：{}毫秒'.format(end - start))
    except:
        print('程序异常，请检查输入数据是否正常')

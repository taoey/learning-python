import os
import time


def split_file(file_num, file_path):
    """
    对大文件进行哈希分割
    :param file_path:
    :return:
    """
    try:
        os.mkdir('files')
    except:
        pass
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for ip in f:
            count = count + 1
            if count % 1000 == 0:
                print('已经处理了条数：{}'.format(count))
            file_index = hash(ip) % 100;
            # 写入IP数据
            with open('files/file{}.txt'.format(file_index), 'a', encoding='utf-8') as split_f :
                split_f.write(ip)
                split_f.close()
        f.close()


def top_one(file_path, min):
    """
    找出小文件中频率最高的IP地址及频率（如果有并列的的返回list）
    :param file_path:
    :param min: 最小频率
    :return:
    """
    ips = {}
    ip_map = {}
    max = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for ip in f:
            if ip not in ip_map:
                ip_map[ip] = 1
            else:
                ip_map[ip] = ip_map[ip] + 1
            # 出现最大频率IP，移除原来所有IP
            if max < ip_map[ip] and max > min:
                ips.clear()
                ips[ip] = ip_map[ip]
                max = ip_map[ip]
            elif max < ip_map[ip] and max <= min:
                max = ip_map[ip]
            # 最大频率IP和当前最大相同，都保存
            elif max == ip_map[ip] and max > min:
                ips[ip] = ip_map[ip]
    return ips



if __name__ == '__main__':
    start = time.clock()

    max = 0
    result = []
    result_map = {}
    file_path = 'data.txt'
    file_num = 100
    split_file(file_num, file_path)
    for i in range(0, file_num):
        ips = top_one('files/file{}.txt'.format(i), 2)
        result_map = dict(result_map, **ips)
    print(result_map)
    for key, value in result_map.items():
        if value > max :
            max = value
            result.clear()
            result.append(key)
        elif value == max :
            result.append(key)
    print(result)
    end = time.clock()
    print('总用时：{}秒'.format(end - start))



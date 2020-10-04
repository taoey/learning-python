import codecs
import csv
import re
import json

def accountMake(payee):
    data = re.findall(r"^(.+?)\s", line[2])[0]
    payee = str(line[7]).replace(" ", "")
    remark = str(line[8]).replace(" ", "")
    number = str(line[9]).replace(" ", "")

    with open('payee_map.json', 'r', encoding='utf-8') as f:
        dict = json.load(fp=f)
        if payee in dict.keys():
            # 构造一条记录
            return str.format("{} * \"{}\" \"{}\"\n\t{}\t+{} CNY\n\t{} -{} CNY\n",
                             data, payee, remark, dict[payee][0], number,dict[payee][1], number)
        else:
            return str.format("{} * \"{}\" \"{}\"\n\t{}\t+{} CNY\n\t{} -{} CNY\n",
                             data, payee, remark, dict["other"][0], number,dict["other"][1], number)


if __name__ == '__main__':
    filename = "alipay_record_20191105_1307_1.csv"
    file_csv = csv.reader(codecs.open(filename, 'r', 'GBK'))
    file_writer = codecs.open('file_out.txt', 'a', 'utf-8')

    for line in file_csv:
        if len(line) > 5 and str(line[0]).find("交易号") < 0:
            account_str = accountMake(line)
            file_writer.write(account_str)
            file_writer.flush()
    file_writer.close()

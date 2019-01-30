#encoding:utf-8
import csv
import codecs

if __name__ == '__main__':
    csv_file = csv.reader(codecs.open('test_data.csv','r','utf-8'))
    for line in csv_file:
        print(line)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import codecs

if __name__ == '__main__':
    filename = "0225_f.csv"
    file_csv = csv.reader(codecs.open(filename, 'r', 'utf-8'))
    file_writer = codecs.open('0225_f', 'a', 'utf-8')
    for line in file_csv:
        print(line[0])
        file_writer.write(line[0] + "\n")
    file_writer.close()

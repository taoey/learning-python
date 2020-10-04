#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def speak(data_str):
    cmd = f"say '{data_str}'"
    os.system(cmd)


if __name__ == '__main__':
    path = 'speak_data.txt'
    file_object = open(path, 'r')
    try:
        for line in file_object:
            line = line.replace('\n','')
            speak(line)

    finally:
        file_object.close()


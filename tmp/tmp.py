#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s1 = "魏文磊🇨🇳🚹💗🚺_1_安道尔__"
    s2 = " \nづ待、陌上花开141319_2_中国_宁夏_银川"
    s3 = "                                  _2_安道尔__"
    s4 = "青春_1_中国_北京_朝阳"
    s5 = "高长老ʚ?ྀིɞ_1_中国_云南_红河"
    s6 = "高长老ʚ🐷ྀིɞ_1_中国_云南_红河"
    print(s5 == s6) # False
    sarr = [s1]
    for s in sarr:
        tmp_byte = ("vadd_gzh_fans2_"+s.rstrip("\n")).encode()
        print(tmp_byte)
    sa = s1.split("_")
    print(len(sa))
    key = "vadd_gzh_fans4_{}_{}_{}_{}_{}".format("\n",2,3,"",5)
    print(key)

    sss = b"\xe8\x88\x91\xe7\x88\xb1python"
    print(sss.decode('UTF-8'))


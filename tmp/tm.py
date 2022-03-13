#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s1 = "魏文磊🇨🇳🚹💗🚺_1_安道尔__"
    sarr = [s1]
    for s in sarr:
        tmp_byte = ("vadd_gzh_fans4_"+s.rstrip("\n")).encode()
        print(tmp_byte)
    sa = s1.split("_")

    print(len(sa))
    key = "vadd_gzh_fans4_{}_{}_{}_{}_{}".format("\n",2,3,"",5)
    print(key)

    sss = b"\xe8\x88\x91\xe7\x88\xb1python"
    print(sss.decode('UTF-8'))
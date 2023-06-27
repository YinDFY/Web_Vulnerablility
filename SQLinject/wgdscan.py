#!/usr/bin/env python
# -*- coding:utf-8 -*-

from SQLinject.lib.core.Spider import SpiderMain


def main(url):
    root = url
    threadNum = 10
    ret = []
    # spider
    wgd = SpiderMain(root, threadNum)
    ret = wgd.craw()
    # print(ret)
    return ret

if __name__ == '__main__':
    main('http://192.168.1.192:8086/pikachu/')

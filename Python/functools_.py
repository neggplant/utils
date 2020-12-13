#!/usr/local/envs/bin/python
# -*- encoding:utf-8 -*-

from functools import partial

def qw(a,b):
    return a+b
# 偏函数，设置默认第一个参数
qq = partial(qw,4)

print(qq(6))

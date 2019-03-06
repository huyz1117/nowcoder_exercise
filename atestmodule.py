#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:55:36 2019

@author: apple
"""

# a test module

def addFunc(a, b):
    return a + b

print(__name__)
# 测试代码
if __name__ == '__main__':
    print('atestmodule计算结果: ', addFunc(1, 2))
    print(__name__)
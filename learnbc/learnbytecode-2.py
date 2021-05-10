#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learnbytecode-2.py

import platform

def sayHello():
    print("hello,world!")
print("python Version:",end="")
print(platform.python_version())
print("---------------------")
codeAttributes=list(dir(sayHello.__code__))
for codeAttr in codeAttributes:
    if "co_" in codeAttr:
        print(codeAttr,end=":")
        print(codeAttr)
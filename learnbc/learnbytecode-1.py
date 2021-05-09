#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learnbytecode-1.py
import dis
import platform

def sayHello():
    print("hello,world!")
print("python Version:",end="")
print(platform.python_version())
print("---------------------")
print(dis.dis(sayHello))
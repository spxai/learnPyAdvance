#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learnbytecode-3-3.py
import marshal, dis

f = open("__pycache__/learnbytecode-3-1.cpython-39.pyc ", "rb")
f.seek(16) # Skip 16 byte header (for Python 3.8)
co = marshal.load(f)
print(dis.dis(co))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learnbytecode-3-4.py
import marshal, dis
import time
import struct
import codecs
import importlib.util
import sys


print (f"python version:{sys.version}")
print(f"magic number:{importlib.util.MAGIC_NUMBER.hex()}")


f = open("__pycache__/learnbytecode-3-1.cpython-39.pyc ", "rb")
magic = f.read(4)
bitField=f.read(4)
moddate = f.read(4)
fileSize=f.read(4)
modtime = time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(struct.unpack('L', moddate)[0])))
print(f"magic {codecs.encode(magic,'hex')}")
print(f"bitField {codecs.encode(bitField,'hex')}")
print(f"moddate :{modtime}")
print(f"fileSize :{codecs.encode(fileSize,'hex')}")
co = marshal.load(f)
print(dis.dis(co))
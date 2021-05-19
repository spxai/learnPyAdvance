#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#learnbytecode-3-5.py
import marshal, dis
import time
import struct
import codecs
import importlib.util
import sys

def getFileInfo(fname):
    import os
    statinfo = os.stat(fname)
    return (statinfo.st_size,int(statinfo.st_mtime))


print (f"python version:{sys.version}")
f = open("__pycache__/learnbytecode-3-1.cpython-39.pyc ", "rb")
magic = f.read(4)
bitField=f.read(4)
moddate = f.read(4)
fileSize=f.read(4)
fileSz=struct.unpack("=L", fileSize)[0]
code=f.read()
modtime = time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(struct.unpack('=L', moddate)[0])))
print(f"magic {codecs.encode(magic,'hex')}")
print(f"bitField {codecs.encode(bitField,'hex')}")
print(f"moddate :{modtime}")
print(f"fileSize :{fileSz}")
f.seek(16)
co = marshal.load(f)
print(dis.dis(co))
f.close()

sFileInfo=getFileInfo("learnbytecode-3-1.py")
magic_generate=importlib.util.MAGIC_NUMBER
bitField_generate=(0).to_bytes(4, byteorder="big")

moddate_generate=struct.pack('=L',sFileInfo[1])
srcFileSize_generate=struct.pack('=L',sFileInfo[0])

f = open("byc-generate/learnbytecode-3-1.cpython-39.pyc","wb")
f.write(magic_generate)
f.write(bitField_generate)
f.write(moddate_generate)
f.write(srcFileSize_generate)
f.write(code)
f.close()

f = open("byc-generate/learnbytecode-3-1.cpython-39.pyc ", "rb")
magic = f.read(4)
bitField=f.read(4)
moddate = f.read(4)
fileSize=f.read(4)
fileSz=struct.unpack("=L", fileSize)[0]
code=f.read()
modtime = time.strftime("%Y-%m-%d %H:%M:%S",(time.localtime(struct.unpack('=L', moddate)[0])))
print(f"magic {codecs.encode(magic,'hex')}")
print(f"bitField {codecs.encode(bitField,'hex')}")
print(f"moddate :{modtime}")
print(f"fileSize :{fileSz}")
f.seek(16)
co = marshal.load(f)
print(dis.dis(co))
f.close()
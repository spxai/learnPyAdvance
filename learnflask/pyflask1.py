#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return r'hello,world<br/>你好，世界<br/>'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return r'hello,world<br/>你好，世界<br/>'

@app.route('/login')
def userLogin():
    return '''
     <form>
			 昵称：<input type="text" name="username" accesskey="n" />
			 <p/>
			 密码: <input type="password" name ="passwd" accesskey="p">
			 <p/>			 
			 <input type="submit" value="登录" accesskey="l"/>
		 </form>
    '''


@app.route('/reg')
@app.route('/usrreg')
def userReger():
    return '''
         <form>
			 昵称：<input type="text" name="username" accesskey="n" />
			 <p/>
			 登录密码: <input type="password" name ="passwd1" accesskey="p">
			 <p/>	
			 确认密码: <input type="password" name ="passwd2" accesskey="p">
			 <p/>			 
			 年龄: <input type="text" name ="passwd" accesskey="p">
			 <p/>					  
			 性别:
			 <select>
			   <option value="man">男</option>
			   <option value="woman">女</option>
			 </select>
			 <p/>	
			 <input type="submit" value="注册" accesskey="r"/>
		 </form>
    '''
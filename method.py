#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cl_test.py
#  
#  Copyright 2019 chenlu <chenlu@CLU>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

message = "Hello python"

#每个单词首字母大写
print(message.title())

#每个字母大写
print(message.upper())

#每个字母小写
print(message.lower())

#合并字符串
print(message.upper() + " nr \r\n " + message.lower())

#input 默认类型字符串
message = input("Enter your name:")
print("Your name is" + " " + message)

#input 转换为整形
age = int(input("Enter yout age:"))

#str 将整数转换成字符串格式
print("Your age is" + " " + str(age))

#去掉字符串前后的空格
#    strip() 同时去掉前后两端的空格
#   lstrip() 只去掉字符串开头的空格
#   rstrip() 只去掉字符串尾部的空格
Name = "   Chen   LU   "
print("Name.strip()  = " + Name.strip())
print("Name.lstrip() = " + Name.lstrip())
print("Name.rstrip() = " + Name.rstrip())









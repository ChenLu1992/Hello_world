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

#ÿ����������ĸ��д
print(message.title())

#ÿ����ĸ��д
print(message.upper())

#ÿ����ĸСд
print(message.lower())

#�ϲ��ַ���
print(message.upper() + " nr \r\n " + message.lower())

#input Ĭ�������ַ���
message = input("Enter your name:")
print("Your name is" + " " + message)

#input ת��Ϊ����
age = int(input("Enter yout age:"))

#str ������ת�����ַ�����ʽ
print("Your age is" + " " + str(age))

#ȥ���ַ���ǰ��Ŀո�
#    strip() ͬʱȥ��ǰ�����˵Ŀո�
#   lstrip() ֻȥ���ַ�����ͷ�Ŀո�
#   rstrip() ֻȥ���ַ���β���Ŀո�
Name = "   Chen   LU   "
print("Name.strip()  = " + Name.strip())
print("Name.lstrip() = " + Name.lstrip())
print("Name.rstrip() = " + Name.rstrip())









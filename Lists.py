#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  列表.py
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


#列表 打印需要str
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("bicycles is " + str(bicycles))
print("\r\n")

#访问列表
print("bicycles[0] is " + bicycles[0])
print("bicycles[0].title is " + bicycles[0].title())
print("\r\n")

#从后往前 访问倒数第一个元素 bicycle[-1]
print("bicycles[-1] is " + bicycles[-1])
print("\r\n")

#修改元素
bicycles[0] = 'Haf'
print("After bicycles[0] = " + bicycles[0])
print("\r\n")

#尾部添加元素
bicycles.append('ducati')
print("bicycles is " + str(bicycles))
print("\r\n")

#使用append动态创建链表
Lists = []
Lists.append('a')
Lists.append('b')
Lists.append('c')
print(str(Lists))
print("\r\n")

#在任意位置插入 insert
Lists.insert(0, 'F')
print(str(Lists))
print("\r\n")

#删除元素 del
del Lists[1]
print(str(Lists))
print("\r\n")

#删除元素后直接使用其值 pop() 不指定索引 默认弹出末尾元素
print(str(bicycles))
popped_bicycle = bicycles.pop()
print("pop() bicycle = " + popped_bicycle)
print("bicycles = " + str(bicycles))
print("\r\n")

#根据值删除元素 remoce() 如果有多个相同值 需要用循环来删除
print(str(bicycles))
bicycles.remove('Haf')
print("remove('Haf') : " + str(bicycles))
print("\r\n")

#永久排序 sort() 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("cars = " + str(cars))
cars.sort() #字典序
print("cars.sort() = " + str(cars))
cars.sort(reverse=True) #反向字典序
print("cars.sort(reverse=True)" + str(cars))
print("\r\n")

#临时排序 sorted()










#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  �б�.py
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


#�б� ��ӡ��Ҫstr
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("bicycles is " + str(bicycles))
print("\r\n")

#�����б�
print("bicycles[0] is " + bicycles[0])
print("bicycles[0].title is " + bicycles[0].title())
print("\r\n")

#�Ӻ���ǰ ���ʵ�����һ��Ԫ�� bicycle[-1]
print("bicycles[-1] is " + bicycles[-1])
print("\r\n")

#�޸�Ԫ��
bicycles[0] = 'Haf'
print("After bicycles[0] = " + bicycles[0])
print("\r\n")

#β�����Ԫ��
bicycles.append('ducati')
print("bicycles is " + str(bicycles))
print("\r\n")

#ʹ��append��̬��������
Lists = []
Lists.append('a')
Lists.append('b')
Lists.append('c')
print(str(Lists))
print("\r\n")

#������λ�ò��� insert
Lists.insert(0, 'F')
print(str(Lists))
print("\r\n")

#ɾ��Ԫ�� del
del Lists[1]
print(str(Lists))
print("\r\n")

#ɾ��Ԫ�غ�ֱ��ʹ����ֵ pop() ��ָ������ Ĭ�ϵ���ĩβԪ��
print(str(bicycles))
popped_bicycle = bicycles.pop()
print("pop() bicycle = " + popped_bicycle)
print("bicycles = " + str(bicycles))
print("\r\n")

#����ֵɾ��Ԫ�� remoce() ����ж����ֵͬ ��Ҫ��ѭ����ɾ��
print(str(bicycles))
bicycles.remove('Haf')
print("remove('Haf') : " + str(bicycles))
print("\r\n")

#�������� sort() 
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("cars = " + str(cars))
cars.sort() #�ֵ���
print("cars.sort() = " + str(cars))
cars.sort(reverse=True) #�����ֵ���
print("cars.sort(reverse=True)" + str(cars))
print("\r\n")

#��ʱ���� sorted()










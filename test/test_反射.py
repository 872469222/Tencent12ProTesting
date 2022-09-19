#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
class Person:

	def __init__(self):
		self.name

	def eat(self):
		print(f"{self.name}is  eating")

p= Person('jerry')

print(hasattr(p, 'name'))
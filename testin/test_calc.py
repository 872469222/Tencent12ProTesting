#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
import unittest

from python.calc import Calc


class TestCal(unittest.TestCase):
	def test_and_1(self):
		self.calc=Calc()
		result=	self.calc.test_abc(1,2)
		print(result)
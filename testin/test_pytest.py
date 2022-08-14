#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
import pytest

# from python.calc
from python.calc import Calc

class TestCalc:
	def test_add_1(self) :
		self.calc =Calc()
		result = self.calc.test_abc(1,2)
		print(result)
		assert 3 == result
	def test_div(self):
		self.calc=Calc()
		result = self.calc.div(2,2)
		assert 1 == result

if __name__ == '__main__':
    pytest.main()
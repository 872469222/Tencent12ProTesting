#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
import pytest
from python.calc import Calc
from decimal import Decimal
class TestCalc:
	def setup(self):
		self.calc=Calc()

	# @pytest.mark.second
	def test_add(self) :
		self.calc =Calc()
		result = self.calc.test_abc(1,2)
		print(result)
		assert 3 == result

	# @pytest.mark.run(order=3)
	# def test_add(self) :
	# 	self.calc =Calc()
	# 	result = self.calc.test_abc(1,2)
	# 	print(result)
	# 	assert 3 == result

	# @pytest.mark.first
	@pytest.mark.parametrize('data1,data2,expect',[
		(1,2,3),
		(0.1, 0.2, 0.3),
		(0, 1, 1),
	])
	def test_add_1(self,data1,data2,expect) :
		self.calc =Calc()
		result = self.calc.test_abc(data1,data2)
		print(result)
		assert expect == result

	# @pytest.mark.run(order=-1)
	def test_div(self):
		self.calc=Calc()
		result = self.calc.div(2,2)
		assert 1 == result

if __name__ == '__main__':
    pytest.main()
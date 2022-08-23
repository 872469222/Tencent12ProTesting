#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 参数化装饰器有一个额外的参数ids，可以标识每一个测试用例，自定义测试数据结果的显示，
# 为了增加可读性，我们可以标记每一个测试用例使用的测试数据是什么，适当的增加一些说明。
# 在使用前你需要知道，ids参数应该是一个字符串列表，必须和数据对象列表的长度保持一致。
import pytest

data_1=[
	(1, 2, 3),
	(4, 5, 9)
]
ids = ["a:{} + b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_1]

def add(a,b):
	return  a + b

@pytest.mark.parametrize('a,b,expect',data_1,ids=ids)
class TestParametrize(object):
	def test_parametrize1(self,a,b,expect):
		print('\n测试函数1测试数据为\n{}-{}'.format(a, b))
		assert add(a,b) == expect
	def test_parametrize2(self,a,b,expect):
		print('\n测试函数2数据为\n{}-{}'.format(a, b))
		assert add(a,b) == expect
if __name__ == '__main__':
    pytest.main(["-v","test_08增加测试结果可读性.py"])
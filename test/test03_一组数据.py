#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 当测试用例需要多个数据时，我们可以使用嵌套序列(嵌套元组&嵌套列表)的列表来存放测试数据。
#
# 装饰器@pytest.mark.parametrize()可以使用单个变量接收数据，也可以使用多个变量接收，同样，测
#
# 试用例函数也需要与其保持一致。
#
# 　　当使用单个变量接收时，测试数据传递到测试函数内部时为列表中的每一个元素或者小列表，需
#
# 要使用索引的方式取得每个数据。
#
# 　　当使用多个变量接收数据时，那么每个变量分别接收小列表或元组中的每个元素列表嵌套多少个多
#
# 组小列表或元组，测生成多少条测试用例。
import pytest
data=[
		[1,2,3],
	    [4,5,9]
]
@pytest.mark.parametrize('a,b,c',data)
# 一个参数接收一个数据
def test_parametrize_1(a,b,c):
	print('\n测试数据为\n{}，{}，{}'.format(a, b, c))
	actual = a + b
	assert actual == c
@pytest.mark.parametrize('value',data)
# 一个参数接收一组数据
def test_parametrize_2(value):
	print('\n测试数据为\n{}'.format(value))
	actual = value[0] + value[1]
	assert actual ==value[2]
if __name__ == '__main__':
    pytest.main(["-s","test03_一组数据.py"])

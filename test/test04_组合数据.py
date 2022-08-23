#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 通过测试结果，我们不难分析，一个测试函数还可以同时被多个参数化装饰器装饰，那么多个
# 装饰器中的数据会进行交叉组合的方式传递给测试函数，进而生成n * n个测试用例。
import pytest

data_1 =[1,2,3]
data_2= ['a','b']

@pytest.mark.parametrize('a',data_1)
@pytest.mark.parametrize('b',data_2)
# @pytest.mark.parametrize('c',data_1)

def test_parametrize1(a,b):
	print(f'笛卡尔积测试结果为：{a},{b}')
if __name__ == '__main__':
    pytest.main(["-vs","test04_组合数据.py"])
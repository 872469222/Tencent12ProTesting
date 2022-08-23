#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 当测试用例只需要一个参数时，我们存放数据的列表无序嵌套序列，
# @pytest.mark.parametrize("name", data)
# 装饰器的第一个参数也只需要一个变量接收列表中的每个元素，第二个参数传递存储数据的列表，那么测试用例需要使用同名的字符串接收测试数据(实例中的name)且列表有多少个元素就会生成并执行多少个测试用例
import pytest


data = ["Rose","white","test","teee","aaaa","bbbb"]

@pytest.mark.parametrize("name",data)
def test_parametrize(name):
    print('\n列表中的名字为\n{}'.format(name))

if __name__ == "__main__":
    pytest.main(["-s","test_07.py"])
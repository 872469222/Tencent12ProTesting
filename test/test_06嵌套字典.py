#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试 test_06嵌套字典.py
# 输出结果显示收集到4个用例，两个通过，一个被跳过，一个标记失败，当我们不想执行某组测试
# 数据时，我们可以标记skip或skipif；当我们预期某组数据会执行失败时，我们可以标记为xfail等。
import pytest
data = (
	{
			'user':"name1",
		    'pwd':123
	},
	{
			'user':'name2',
			'pwd':456
	}
)
@pytest.mark.parametrize('dict',data)
def test_parametrize(dict):
	print('\n测试数据为\n{}'.format(dict))

if __name__ == '__main__':
    pytest.main(["-vs","test_06嵌套字典.py"])




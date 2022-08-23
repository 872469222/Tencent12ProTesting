#!/usr/bin/python 
# -*- coding: UTF-8 -*-
# Author:测试
# 输出结果显示收集到4个用例，两个通过，一个被跳过，一个标记失败，当我们不想执行某组测试
# 数据时，我们可以标记skip或skipif；当我们预期某组数据会执行失败时，我们可以标记为xfail等。
import pytest
@pytest.mark.parametrize("test_input,expected",[
    ("3+5",8),
    ("2+4",6),
    pytest.param("6 * 9",42,marks=pytest.mark.xfail),
    pytest.param("6 * 6",42,marks=pytest.mark.skip)
])
def test_mark(test_input,expected):
    assert eval(test_input) == expected
if __name__ == '__main__':
    pytest.main(["-vs","test05_标记用例.py"])
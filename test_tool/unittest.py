# unittest类似于流行的Java测试框架JUnit，它比doctest更灵活，更强大，能够帮助你以结构化的方式来编写庞大而详尽的测试集。
# 我们以一个简单的示例入手，首先我们编写my_math.py脚本，代码如下：

# -*- coding: utf-8 -*-
def product(x, y):
    '''
    :param x: int, float
    :param y: int, float
    :return:  x * y
    '''
    return x * y
# 该函数实现的功能为：输入两个数x, y， 返回这两个数的乘积。接着是test_my_math.py脚本，完整的代码如下：

import unittest

class ProductTestcase(unittest.TestCase):

    def setUp(self):
        print('begin test')

    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = product(x, y)
                self.assertEqual(p, x*y, 'integer multiplication failed')

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x/10
                y = y/10
                p = my_math.product(x, y)
                self.assertEqual(p, x * y, 'integer multiplication failed')

if __name__ == '__main__':
    unittest.main()
# 函数unittest.main负责替你运行测试：在测试方法前执行setUp方法，示例化所有的TestCase子类，并运行所有名称以test打头的方法。assertEqual方法检车指定的条件（这里是相等），以判断指定的测试是成功了还是失败了。
#   接着，我们运行前面的测试，输出的结果如下：

# begin test
# .begin test
# .
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# OK
# 可以看到，该程序运行了两个测试，每个测试前都会输出'begin test'，.表示测试成功，若测试失败，则返回的是F。
# 接着模拟测试出错的情形，将my_math函数中的product方法改成返回：
# return x + y
# 再运行测试脚本，输出的结果如下：

# begin test
# Fbegin test
# F
# ======================================================================
# FAIL: test_floats (__main__.ProductTestcase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_my_math.py", line 20, in test_floats
#     self.assertEqual(p, x * y, 'integer multiplication failed')
# AssertionError: -2.0 != 1.0 : integer multiplication failed

# ======================================================================
# FAIL: test_integers (__main__.ProductTestcase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_my_math.py", line 12, in test_integers
#     self.assertEqual(p, x*y, 'integer multiplication failed')
# AssertionError: -20 != 100 : integer multiplication failed

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=2)
# 两条测试都未通过，返回的是F，并帮助你指出了错误的地方，接下来，你应该能快速地修复这个bug。


# 关于unittest模块的更加详细的说明，可以参考网址：https://docs.python.org/3/library/unittest.html 。
# doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。
# 下面我们以doctest.testmod为例，函数doctest.testmod会读取模块中的所有文档字符串，
# 查找看起来像是从交互式解释器中摘取的示例，再检查这些示例是否反映了实际情况。

# -*- coding: utf-8 -*-

def string_lower(string):
    '''
    返回一个字符串的小写
    :param string: type: str
    :return: the lower of input string
    >>> string_lower('AbC')
    'abc'
    >>> string_lower('ABC')
    'abc'
    >>> string_lower('abc')
    'abc'
    '''
    return string.lower()

if __name__ == '__main__':
    import doctest, test_string_lower
    doctest.testmod(test_string_lower)
# 首先先对程序进行说明，函数string_lower用于返回输入字符串的小写，
# 函数中的注释中，一共包含了3个测试实例，期望尽可能地包含各种测试情况，
# 接着在主函数中导入doctest, test_string_lower，再运行doctest中的testmod函数即可进行测试。
# 接着，我们开始测试。首先，在命令行中输入python test_string_lower.py，运行后会发现什么都没有输出，但这其实是件好事，它表明程序中的所有测试都通过了！那么，如果我们想要获得更多的输出呢？可在运行脚本的时候增加参数-v，这时候命令变成python test_string_lower.py -v，输出的结果如下：

# Trying:
#     string_lower('AbC')
# Expecting:
#     'abc'
# ok
# Trying:
#     string_lower('ABC')
# Expecting:
#     'abc'
# ok
# Trying:
#     string_lower('abc')
# Expecting:
#     'abc'
# ok
# 1 items had no tests:
#     test_string_lower
# 1 items passed all tests:
#    3 tests in test_string_lower.string_lower
# 3 tests in 2 items.
# 3 passed and 0 failed.
# Test passed.
# 可以看到，程序测试的背后还是发生了很多事。接着，我们尝试着程序出错的情况，比如我们不小心把函数的返回写成了：
# return string.upper()
# 这其实是返回输入字符串的大写了，而我们测试的实例却返回了输入字符串的小写，再运行该脚本（加上参数-v），输出的结果如下：

# Failed example:
#     string_lower('abc')
# Expected:
#     'abc'
# Got:
#     'ABC'
# 1 items had no tests:
#     test_string_lower
# **********************************************************************
# 1 items had failures:
#    3 of   3 in test_string_lower.string_lower
# 3 tests in 2 items.
# 0 passed and 3 failed.
# ***Test Failed*** 3 failures.
# 这时候，程序测试失败，它不仅捕捉到了bug，还清楚地指出错误出在什么地方。我们不难把这个程序修改过来。



#   关于doctest模块的更详细的使用说明，可以参考网址：https://docs.python.org/2/library/doctest.html 。
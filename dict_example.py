#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 删除字典元素的4种方法

# 清空词典所有条目
def clear_test():
    dict = {'name': '我的博客地址', 'alexa': 10000, 'url': 'http://blog.csdn.net/uuihoo/'}
    dict.clear()

 # 删除要删除的键值对，如{'name':'我的博客地址'}这个键值对
def pop_test():
    site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
    pop_obj=site.pop('name')
    print(pop_obj)   # 输出 ：我的博客地址

# 随机返回并删除一个键值对
def popitem_test():
    site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
    pop_obj=site.popitem() # 
    print(pop_obj)   # 输出结果可能是{'url','http://blog.csdn.net/uuihoo/'}

# del 全局方法（能删单一的元素也能清空字典，清空只需一项操作）
def del_test():
    site= {'name': '我的博客地址', 'alexa': 10000, 'url':'http://blog.csdn.net/uuihoo/'}
    del site['name'] # 删除键是'name'的条目 
    del site  # 清空字典所有条目
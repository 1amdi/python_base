# -*- coding: utf-8 -*-

# example 2-1 字符串转unicode码位列表 for循环
import array

symbols = '$¥€'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# example 2-2 列表推导式
codes = [ord(symbol) for symbol in symbols]
print(codes)

# example 2-4 列表推导计算笛卡尔积
# example 2-3 列表推导式条件判断
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

# example 2-4 列表推导计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# example 2-5 生成器表达式初始化元组和数组
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))

# example 2-6 生成器表达式计算笛卡尔积
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

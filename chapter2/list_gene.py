# -*- coding: utf-8 -*-

#example 2.1 字符串转unicode码位列表 for循环

symbols ='$¥€'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
print(codes)



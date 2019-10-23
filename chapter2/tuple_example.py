
# example 2-7 吧元组作为记录，无用元素赋给_  p65
import os

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country,_ in traveler_ids:
    print(country)

_,filname = os.path.split('/Users/xiangjun/.ssh/id_rsa.pub')
print(filname)

# *处理剩余元素
a, b, *rest = range(5)
print(a, b, rest)

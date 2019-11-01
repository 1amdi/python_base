# example 2-7 吧元组作为记录，无用元素赋给_  p65
import os
from collections import namedtuple

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

_, filname = os.path.split('/Users/xiangjun/.ssh/id_rsa.pub')
print(filname)

# *处理剩余元素
a, b, *rest = range(5)
print(a, b, rest)

# 平行赋值，*只能用在一个变量前，但是此变量可出现在赋值表达式中的任意位置
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(head, b, c, d)

# example 2-8 元组拆包
metra_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delphi NCR', 'IN', 21.935, (28.613899, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -19.133333)),
    ('New York-Neward', 'US', 20.104, (40.189789, -70.023107)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635458)),
]
print('{:15} | {:^9} | {:9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metra_areas:
    if longitude < 0:
        print(fmt.format(name, latitude, longitude))

# example 2-9 定义和使用具名元组
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.453, (35.68973, 139.69167))
print(tokyo)
print(tokyo.population)
tokyo = City(name='Tokyo', country='JP', population=36.453, coordinates=(35.68973, 139.69167))
print(tokyo[1])

# example 2-10 具名元组的属性和方法
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.61399, 77.0288889))
delhi = City._make(delhi_data)
# print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ': ' + value)

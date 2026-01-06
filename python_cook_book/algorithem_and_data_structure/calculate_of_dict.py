prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}
print(list(zip(prices.values(), prices.keys())))# [(45.23, 'ACME'), (612.78, 'AAPL'), (205.55, 'IBM'), (37.2, 'HPQ'), (10.75, 'FB')]
"""
    将字典的键值对翻转过来，用zip凑成可迭代对象，再寻找最大/小值
    可迭代对象中的值一般会决定返回对象，如果值相同，则由键决定返回对象
    prices = {'AA':45.23,'ZZ':45.23}
    min = min(zip(prices.values(), prices.keys()))  # >> (45.23, 'AA')
    max = max(zip(prices.values(), prices.keys()))  # >> (45.23, 'ZZ')

"""

min_price = min(zip(prices.values(), prices.keys())) 

max_price = max(zip(prices.values(), prices.keys()))



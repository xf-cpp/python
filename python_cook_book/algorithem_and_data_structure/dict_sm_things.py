from collections import OrderedDict

def calculate_of_dict():
    """
    将字典的键值对翻转过来，用zip凑成可迭代对象，再寻找最大/小值
    可迭代对象中的值一般会决定返回对象，如果值相同，则由键决定返回对象
    prices = {'AA':45.23,'ZZ':45.23}
    min = min(zip(prices.values(), prices.keys()))  # >> (45.23, 'AA')
    max = max(zip(prices.values(), prices.keys()))  # >> (45.23, 'ZZ')

    """
    prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
    }
    print(list(zip(prices.values(), prices.keys())))# [(45.23, 'ACME'), (612.78, 'AAPL'), (205.55, 'IBM'), (37.2, 'HPQ'), (10.75, 'FB')]
    min_price = min(zip(prices.values(), prices.keys())) 
    max_price = max(zip(prices.values(), prices.keys()))


def orderd_dict():
    """
    排序字典
    """
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])


def find_same_key_or_value_in_dict():
    """
    
    """
    a = { 'x' : 1,
          'y' : 2,
          'z' : 3,
         }
    b = { 'w' : 1,
          'y' : 2,
          'z' : 3,
         }
    # 寻找a b字典中相同的键
    print( a.keys() & b.keys())  # {'y', 'z'}
    # 寻找a中和b中不同的键
    print(a.keys() - b.keys())  #{'x'}
    # 寻找 a b中相同的键值对
    print(a.items() & b.items()) #{('z', 3), ('y', 2)}

if __name__ == '__main__':
    # orderd_dict()
    # calculate_of_dict()
    find_same_key_or_value_in_dict()





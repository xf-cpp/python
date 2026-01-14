from collections import OrderedDict
def orderd_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])

if __name__ == '__main__':
    orderd_dict()
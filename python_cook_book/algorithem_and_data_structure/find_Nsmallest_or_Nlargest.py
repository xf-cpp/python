import heapq
def basic_usage()->None:
    """
    heapq.nsmallest
    heapq.largest 基础用法及测试
    """
    example_list = [1,2,23,7,-4,18,23,42,37,2]  # 数字组成的列表
    example_dict = [
        {'name':'IBM', 'share':100, 'price':91.1},
        {'name':'AAPL', 'share':50, 'price':543.22},
        {'name':'FB', 'share':200, 'price':21.09},
        {'name':'HPQ', 'share':35, 'price':31.75},
        {'name':'YHOO', 'share':45, 'price':16.35},
        {'name':'ACME', 'share':75, 'price':115.65},
        {'name':'ABCD', 'share':100, 'price':91.1},
    ]  #字典组成的列表
    Nsmallest = heapq.nsmallest(3, example_list) # 取可迭代对象中的三个最小值
    Nlargest  = heapq.nlargest(3,example_list)  # 取可迭代对象中的三个最大值

    Nsmallest_from_key = heapq.nsmallest(3, example_dict, key = lambda x:x['share'])  #添加关键字进行排序 然后取最小的三个值
    Nlargest_from_key = heapq.nlargest(3, example_dict, key = lambda x:x['share'])  #添加关键字进行排序 然后取最大的三个值
    print(f'Nsmallest_list is {Nsmallest}') 
    print(f'Nlargest_list is {Nlargest}')
    print(f'Nsmallest_dict is {Nsmallest_from_key}')
    print(f'Nlargest_dict is {Nlargest_from_key}')


class PriorityQueue:
    """
    优先级队列实现
    """
    def __init__(self):
        self._queue = []  # 空列表可直接作为初始堆使用。若有一个非空的列表，要heapq.heapify(heap) 初始列表为堆结构再用heappush和heappop
        self._index = 0  #_index 解决同优先级元素的比较问题（避免元组前两位相同时报错）

    def push(self, item, priority):
        """
        Docstring for push
        
        :param self: Description
        :param item: Description
        :param priority: Description
        """
        # heappush 支持插入元组，(优先级, 索引, 元素)
        # 元组会按「第一个元素→第二个元素→…」的顺序比较, 若优先级能比出大小，则按优先级入堆，否则比较第二元素、第三元素
        self._index += 1
        heapq.heappush(self._queue, (-priority, self._index, item)) # 堆中的实际元素是这个入堆的元祖

    def pop(self):
        # heapq.heappop：弹出堆中最小元素（即 -priority 最小 → 原优先级最高）；
        # heappop(self._queue) -> 
        # [-1]：取三元组的最后一位（实际的 item 对象），屏蔽堆内部的优先级 / 索引细节
        return heapq.heappop(self._queue)[-1]

class Item:
    """
    优先级队列的元素
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

def priority_queue_usage()->None:
    """
    优先级队列用法
    """
    q = PriorityQueue() 
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    

    pass


if __name__ == '__main__':
    priority_queue_usage()

    pass










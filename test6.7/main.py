def cal_sum_in_list(list= []):
    sum = 0
    for i in list:
        sum += i
    return sum

def cal_even_number(start, end):
    even_number = []
    for i in range(start, end):
        if i % 2 == 0:
            even_number.append(i)
    return even_number

def remove_certain_num(origin_list, remove_list):
    for r_num in remove_list:
        if r_num in origin_list:
            origin_list.remove(r_num)
    return origin_list


def remove_repeat_element(list1):
    b = set()
    result = []
    for num in list1:
        b.add(num)
    list(set(list1))
    return result

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 1, 2]
    b = set()
    list(b)
    print(remove_repeat_element(list1))
    # print(cal_sum_in_list(list))
    # print(cal_even_number(4, 15))





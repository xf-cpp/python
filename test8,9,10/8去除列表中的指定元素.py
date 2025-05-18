def remove_b(a, b ):
    new_a = []
    for ele_a in a:
        new_a.append(ele_a)
        for ele_b in b:
            if ele_b == ele_a:
                new_a.pop()
    return new_a

def remove_b_test(a, b):
    for item in a:
        print(item)
        if item in b:
            a.remove(item)
    return a

def best_remove_b(a, b):
    return [item for item in a if item not in b]


if __name__ == '__main__':
    """
        test
    """
    a = [1, 3, 1, 5, 7, 9, 11]
    b = [1, 5, 11]
    c = best_remove_b(a, b)
    print(c)


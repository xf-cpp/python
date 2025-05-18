def remove_duplicate(a):
    b = set(a)
    return list(b)

def remove_duplicate2(a):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result

if __name__ == '__main__':

    a = [1, 3, 1, 5,5, 7, 9, 11, 9 ]
    b = [1, 5, 11]
    c = remove_duplicate2(a)
    print(c)


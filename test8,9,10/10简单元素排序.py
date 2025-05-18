def sort(a, reverse = False):
    sorted_a = sorted(a, reverse = reverse)
    return sorted_a

def remove_duplicate2(a):
    result = []
    for item in a:
        if item not in result:
            result.append(item)
    return result

if __name__ == '__main__':

    a = [50,40,30,20,10 ]
    b = ['dd', 'cc','bb', 'aa']
    c = sort(b, reverse= False)
    print(c)


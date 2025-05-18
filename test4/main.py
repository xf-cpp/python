def calculate_number(start, end):

    for i in range(start,end,1):
        isflag = False
        for j in range(i+1):
            if j == 0 :
                j = j+1
            if i % j == 0 and j != 1 and j != i :
                isflag = False
                break
            isflag = True
        if isflag is True:
            print(i)

if __name__ == '__main__':
    calculate_number(11, 25)

import os







if __name__ == '__main__':
    file_path = r'./12example'
    save_path = r'./12output'
    b = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        # print(file)
        for line in file:
            line = line[:-1]
            b.append(line.split(','))
        print(b)
        sorted_S = sorted(b, key = lambda x:int(x[2]))
        print(sorted_S)
    with open(save_path, 'w', encoding='UTF-8') as file:
        for data in sorted_S:
            # out = data[0]+','+data[1] + ',' + data[2] + '\n'
            file.write(','.join(data) + '\n')
            # file.write(out)

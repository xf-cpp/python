def read_file(path):
    data = []
    with open(path,'r') as fin:
        for line in fin:
            line = line[:-1]
            grade = int(line.split(',')[-1])
            data.append(grade)
    return data

def processData(data):
    max_Score = max(data)
    min_Score = min(data)
    average = sum(data) / len(data)
    print(f'max:{max_Score}, min{min_Score}, average:{average}')







if __name__ == '__main__':
    PATH = r'./12example'
    data = read_file(PATH)
    processData(data)

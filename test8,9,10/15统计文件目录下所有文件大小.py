import os





if __name__ == '__main__':
    path = r'./'
    size = 0
    for file in os.listdir(path):
        if os.path.isfile(file):
            print(os.path.getsize(file))

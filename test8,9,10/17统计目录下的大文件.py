import os













if __name__ =='__main__':
    result_files = []
    root = r'E:\\'
    for root, dirs, files in os.walk(root):
        for file in files:
            file_path = f'{root}/{file}'
            result_files.append((file_path, os.path.getsize(file_path)))
            # os.path.getsize()
    print(
        sorted(result_files, key = lambda x:x[1],reverse=True)[:10]
    )
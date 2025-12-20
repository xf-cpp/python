import logging
from loggertest2 import time2s
def set_up_logger():
        # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置全局日志级别

    # 格式化器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 文件处理器（输出到文件）
    file_handler = logging.FileHandler('test.log', mode='w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # 控制台处理器（输出到控制台）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # 控制台可以只输出INFO及以上级别
    console_handler.setFormatter(formatter)

    # 添加处理器到日志器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def time1s():
    import time
    start = time.time()
    time.sleep(0.5)
    end = time.time()
    logging.info(f'cost {end-start:.2f}s')

    

if __name__ == '__main__':
    set_up_logger()
    for i in range(10):
        time1s()  # 等待1秒
        print(f"{'*'*10}第{i}次{'*'*10}", end='\r')
    for i in range(5):
        time2s(i)
        print(f"{'*'*10}第{i}次{'*'*10}", end='\r')












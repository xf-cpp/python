import logging
# 配置日志级别（默认为WARNING及以上）
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
    )








if __name__ == '__main__':


    # 记录不同级别的日志
    logging.debug("这是一条调试信息")    # 不会显示，因为级别低于INFO
    logging.info("这是一条普通信息")     # 会显示
    logging.warning("这是一条警告信息")  # 会显示
    logging.error("这是一条错误信息")    # 会显示
    logging.critical("这是一条严重错误信息")  # 会显示



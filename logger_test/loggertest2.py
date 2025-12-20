import logging

import time
def time2s(num):
    set_up_logger(num)
    start = time.time()
    time.sleep(2)
    end = time.time()
    logging.info(f'timer2 cost {end-start:.2f}s')








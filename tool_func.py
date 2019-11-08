
# 计算运行时间的装饰器
import time
def timer(func):
    def wrapper(*args,**kwds):
        t0 = time.time()
        func(*args,**kwds)
        t1 = time.time()
        print('wrapper耗时%0.3f'%(t1-t0,))
    return wrapper

@timer
def do_something(delay):
    print('函数do_something开始')
    time.sleep(delay)
    print('函数do_something结束')

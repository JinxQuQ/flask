# 3.2 不使用装饰器
# 对于这个需求，我们先不使用装饰器，仅使用 Python 的基础语法完成任务，如下所示：

import time


def quick_sort():
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    print('%.4f seconds' % (end_time - start_time))


# 引入 time 模块，需要使用 sleep 方法；在函数的头部，记录开始时间 start_time； 在函数的尾部，记录结束时间 end_time；打印开始时间和结束时间的差，即函数的执行时间。

def bubble_sort():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    print('%.4f seconds' % (end_time - start_time))


def select_sort():
    start_time = time.time()
    time.sleep(3)
    end_time = time.time()
    print('%.4f seconds' % (end_time - start_time))


# 使用同样的方法，对 bubble_sort 和 select_sort 进行修改。

quick_sort()
bubble_sort()
select_sort()
# 依次调用 quick_sort、bubble_sort、select_sort，打印它们各自的运行时间，程序输出如下：
#
# 1.00 seconds
# 2.00 seconds
# 3.00 seconds

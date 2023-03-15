# 3.3 使用装饰器
# 在上一个小节中，我们没有使用装饰器同样完成了需求，但是这样做存在一个明显的问题：
#
# quick_sort、bubble_sort、select_sort 存在代码重复；
# 在函数头部记录开始时间、在函数尾部记录结束时间，逻辑是完全相同的。
# 而通过使用装饰器，可以消除代码重复，代码如下：

import time


def quick_sort():
    time.sleep(1)


def bubble_sort():
    time.sleep(2)


def select_sort():
    time.sleep(3)


# 在上一节的例子中，需要对 quick_sort、bubble_sort 和 select_sort 进行修改。在本节的例子中，不对 quick_sort、bubble_sort 和 select_sort 进行任何修改。

def decorate(input_sort):
    def output_sort():
        start_time = time.time()
        input_sort()
        end_time = time.time()
        print('%.2f seconds' % (end_time - start_time))

    return output_sort


# 装饰器 decorate 是一个高阶函数，输入参数 input_sort 是一个排序函数，返回值是 output_sort 一个功能增强的排序函数。
#
# 在第 3 行，在 output_sort 函数的头部，记录开始时间，调用原排序函数 input_sort；在第 5 行，在 output_sort 函数的尾部，记录结束时间。

quick_sort = decorate(quick_sort)
bubble_sort = decorate(bubble_sort)
select_sort = decorate(select_sort)

# 使用 decorate (quick_sort)，生成一个功能增强的 quick_sort，并替换原有的 quick_sort；使用 decorate (bubble_sort)，生成一个功能增强的 bubble_sort，并替换原有的 bubble_sort；使用 decorate (select_sort)，生成一个功能增强的 select_sort，并替换原有的 select_sort。

quick_sort()
bubble_sort()
select_sort()
# 依次调用 quick_sort、bubble_sort、select_sort，打印它们各自的运行时间，程序输出如下：
#
# 1.00 seconds
# 2.00 seconds
# 3.00 seconds

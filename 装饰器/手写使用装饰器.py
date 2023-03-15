import time


def decorate(input_sort):
    def output_sort():
        start_time = time.time()
        input_sort()
        end_time = time.time()
        print("%.2f" % (end_time - start_time))

    return output_sort


@decorate
def sort1():
    time.sleep(1)


@decorate
def sort2():
    time.sleep(2)


@decorate
def sort3():
    time.sleep(3)


# test=decorate(sort1)
# test()
sort1()
sort2()
sort3()

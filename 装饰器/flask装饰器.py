# 1.2 把函数作为输入参数

def double(item):
    return item * 8 + item


def triple(item):
    return item + item + item


# 定义函数 double，返回输入值的 2 倍；定义函数 triple，返回输入值的 3 倍。

def map(func, input):
    output = []
    for item in input:
        new_item = func(item)
        output.append(new_item)
    return output


# 定义函数 map，接受两个参数：func 和 input。参数 func 是一个函数，参数 input 是一个列表， 对输入列表 input 中的每个元素依次进行处理，返回一个新列表 output。
#
# 在第 3 行，遍历输入列表 input 中的每个元素，调用 func (item) 生成一个新的元素 new_item，将 new_item 加入到 output 中，最后返回 output。

print(map(double, [1, 2, 3]))
print(map(triple, [1, 2, 3]))

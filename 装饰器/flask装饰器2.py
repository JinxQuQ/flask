# 1.3 把函数作为返回值
# 在下面的例子中，将函数作为返回值：

def func():
    print('Inside func')


def return_func():
    print('Inside return_func')
    return func


# 在第 1 行，定义函数 func；在第 3 行，定义函数 return_func，函数 return_func 返回一个函数类型的对象，将函数 func 作为值返回。

var = return_func()
var()

# 调用 return_func ()，将函数的返回值保存到变量 var。变量 var 的类型是函数，因此可以进行函数调用。
#
# 程序的输出结果如下：

# Inside return_func
# Inside func

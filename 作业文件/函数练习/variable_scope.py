x="南水北调工程"
def function1():
    x="南水北调"
    print(x)

def function2():
    #y=x
    # 报错：NameError: name 'x' is not defined
    # 原因：x 是在 function1 的【函数体内部】创建的，属于【局部变量】，
    #       只在 function1 运行期间有效，函数一结束就被销毁了。
    #       function2 是另一个独立的空间，看不见 function1 里的 x，
    #       就像两个不同的班级，1班的同学名单2班是没有的。
    # 想让两个函数共用一个数据，要么把 x 定义在所有函数外面（全局变量），
    # 要么用参数传进去：def function2(x): ...
    x="西气东输"
    print(x)

function1()
function2()
print(x)
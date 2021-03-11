import timeit

# 1. 重复元素判定
# 以下方法可以检查给定列表是不是存在重复元素，它会使用 set() 函数来移除所有重复元素。
def all_unique(lst):
    return len(lst) == len(set(lst))
def test_all_unique():
    x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
    y = [1, 2, 3, 4, 5]
    print(all_unique(x))  # False
    print(all_unique(y))  # True

# 解包
# 如下代码段可以将打包好的成对列表解开成两组不同的元组。
def zip2tuple():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]
    zipped = list(zip(a, b))  # 打包为元组的列表
    print(zipped)
    # [(1, 4), (2, 5), (3, 6)]
    zipped2 = list(zip(a, c))  # 元素个数与最短的列表一致
    print(zipped2)
    # [(1, 4), (2, 5), (3, 6)]
    transposed = list(zip(*zipped))  # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
    print(transposed)
    # [(1, 2, 3), (4, 5, 6)]

# 压缩
# 这个方法可以将布尔型的值去掉，例如（False，None，0，“”），它使用 filter() 函数。
def compact():
    lst = [0, 1, False, 2, '', 3, 'a', 's', 34]
    print(list(filter(bool, lst)))
    # [ 1, 2, 3, 'a', 's', 34 ]


# 17. 链式函数调用
# 你可以在一行代码内调用多个函数。
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def chainfunc():
    a, b = 4, 5
    print((subtract if a > b else add)(a, b)) # 9


# 合并两个字典
# 下面的方法将用于合并两个字典。
def merge_two_dicts(a, b):
    return {**a, **b}
def test_merge_two_dicts():
    a = {'x': 1, 'y': 2}
    b = {'y': 3, 'z': 4}
    print(merge_two_dicts(a, b))
    # {'y': 3, 'x': 1, 'z': 4}


# 将两个列表转化为字典
# 如下方法将会把两个列表转化为单个字典。
def to_dictionary(keys, values):
    return dict(zip(keys, values))
def test_to_dictionary():
    keys = ["a", "b", "c"]
    values = [2, 3, 4]
    print(to_dictionary(keys, values))
    # {'a': 2, 'c': 4, 'b': 3}


# Shuffle
# 该算法会打乱列表元素的顺序，它主要会通过 Fisher-Yates 算法对新列表进行排序：
from copy import deepcopy
from random import randint
def shuffle(lst):
    temp_lst = deepcopy(lst)
    m = len(temp_lst)
    while m:
        m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
    return temp_lst
def test_shuffle():
    foo = [1, 2, 3]
    print(shuffle(foo))  # [2,3,1] , foo = [1,2,3]


def performanceFunc(func:callable) -> None:
    start_time = timeit.default_timer()
    func()
    print(func.__name__)
    print(timeit.default_timer() - start_time)

if __name__ == "__main__":
    # performanceFunc(test_all_unique)
    # performanceFunc(zip2tuple)
    # performanceFunc(compact)
    performanceFunc(test_shuffle)
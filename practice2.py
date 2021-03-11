import time

def processing():
    """ 创建一个进度条 """
    from progress.bar import Bar
    bar = Bar('Processing', max=20)
    for i in range(20):
        # Do some work
        time.sleep(5)
        bar.next()
    bar.finish()

def intersect(num1, num2):
    import collections
    a, b  = map(collections.Counter, (num1, num2))
    # c = {x:num1.count(x) for x in num1}
    return list((a & b).elements())

def intersect_test():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    list1 = intersect(arr1, arr2)
    print(list1)

if __name__ == '__main__':
    intersect_test()
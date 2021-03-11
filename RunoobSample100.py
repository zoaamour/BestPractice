import timeit

def sample32():
    """按相反的顺序输出列表的值。"""
    a = ['one', 'two', 'three']
    print(a[::-1])

def sample25():
    """题目：求1+2!+3!+...+20!的和。"""
    l = range(1, 21)
    def op(x):
        r = 1
        for i in range(1, x + 1):
            r *= i
        return r
    s = sum(map(op, l))
    print('1! + 2! + 3! + ... + 20! = %d' % s)

def sample25_1():
    """题目：求1+2!+3!+...+20!的和。"""
    n = 0
    s = 0
    t = 1
    for n in range(1, 21):
        t *= n
        s += t
    print('1! + 2! + 3! + ... + 20! = %d' % s)


def sample35():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)
    print(bcolors.HEADER + bcolors.OKBLUE + "HEADER")
    print("abc")

def sample44():
    import numpy as np
    x = np.array([[12, 7, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    y = np.array([[5, 8, 1],
                  [6, 7, 3],
                  [4, 5, 9]])
    z = x + y
    print(z)

def performanceTest(func:callable) -> None:
    start_time = timeit.default_timer()
    func()
    print(func.__name__)
    print(timeit.default_timer() - start_time)

if __name__ == "__main__":
    performanceTest(sample25)
    performanceTest(sample25_1)
    # sample32()
    # sample35()
    # sample44()


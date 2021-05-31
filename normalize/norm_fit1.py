import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import matplotlib.mlab as mlab
import seaborn as sns

# %matplotlib inline
sns.set(context='notebook', font='simhei', style='whitegrid')  # 设置风格尺度和显示中文

# import warnings
#
# warnings.filterwarnings('ignore')  # 不发出警告
# 直方图
from scipy.stats import norm  # 使用直方图和最大似然高斯分布拟合绘制分布

# rs=np.random.RandomState(50)#设置随机数种子
# s=pd.Series(rs.randn(100)*100)
s = np.loadtxt('D:/dis.txt')

mu = np.mean(s)  # 计算均值
sigma = np.std(s)
num_bins = 50  # 直方图柱子的数量
n, bins, patches = plt.hist(s, num_bins, normed=1, facecolor='blue', alpha=0.5)
# 直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
y = norm.pdf(bins, mu, sigma)  # 拟合一条最佳正态分布曲线y
str = 'Histogram : $\mu=5.8433$' + str(mu) + ',$\sigma=0.8253$'

plt.plot(bins, y, 'r--')  # 绘制y的曲线
plt.xlabel('sepal-length')  # 绘制x轴
plt.ylabel('Probability')  # 绘制y轴
plt.title(r'Histogram : $\mu={}$,$\sigma={}$'.format(mu, sigma))  # 在题目中显示mu与sigma

plt.subplots_adjust(left=0.15)  # 左边距
plt.show()

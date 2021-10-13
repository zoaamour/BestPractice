import pandas as pd
import numpy as np
from loguru import logger

# 先创建一个简单的 DataFrame 实例
# Terry, Hardon, Curry, Duran, James 和 Barter 代表东西部玩三打三
# 用一组数据记录各自的得分情况
players=['Garsol','Hardon','Bill','Duran','James','Barter']
scores=[22,34,12,31,26,19]
teams=['West','West','East','West','East','East']
df=pd.DataFrame({'player':players,'score':scores,'team':teams})
print(df)

df.team.astype('category')
print(df)

d=pd.Series(scores).describe()
score_ranges=[d['min']-1,d['mean'],d['max']+1]
score_labels=['Role','Star']
# 用pd.cut(ori_data, bins, labels) 方法
# 以 bins 设定的画界点来将 ori_data 归类，然后用 labels 中对应的 label 来作为分类名
df['level']=pd.cut(df['score'],score_ranges,labels=score_labels)
print('df :')
print(df)
print('\n对比一下 Category 类型的数据和普通的 DataFrame中的列有什么区别')
print('\ndf[\'team\'] 是普通的 DataFrame列')
print(df['team'])
print('\ndf[\'level\'] 是 Category 类型的')
print(df['level'])
print('\n可以看出 df[\'level\'] 有点像是集合，输出信息会去重后列出组成元素')
print(df['level'])

import os

import numpy as np
import pandas as pd

from util.ConstUtil import DATA_PATH


class BaseData:
	def __init__(self):
		self.data_path = os.path.join(DATA_PATH, 'cache')
		os.makedirs(self.data_path, exist_ok=True)


df = pd.DataFrame(np.arange(20).reshape(4,5))
print(df)

bs = BaseData()
fpath = os.path.join(bs.data_path, 'foo.pkl')
df.to_pickle(fpath)
print(f'{fpath} has been saved.')

df1:pd.DataFrame = pd.read_pickle(fpath)
print(df1)


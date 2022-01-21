import os
import pandas as pd
import numpy as np


class BaseData:
	def __init__(self):
		LOCALAPPDATA = os.path.expandvars('%LOCALAPPDATA%')
		bookmark_path = r'Microsoft\Edge\User Data\Default\Bookmarks'
		self.fpath = os.path.join(LOCALAPPDATA, bookmark_path)


def main():
	bs = BaseData()
	df = pd.read_json(bs.fpath)
	pass


if __name__ == '__main__':
	main()

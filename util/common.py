import matplotlib.pyplot as plt
import os
import hdf5storage
import numpy as np
import datetime
from util.ConstUtil import GLOBAL_CONFIG


def plt_setting(rcParams:plt.rcParams):
	rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	rcParams['figure.facecolor'] = 'white'
	# rcParams['figure.figsize'] = (10.0, 6.0)


def xscroll():
	fig = plt.figure()
	def OnScroll(event):
		axtemp = event.inaxes
		x_min, x_max = axtemp.get_xlim()
		xunit = (x_max-x_min)/10
		if event.button == 'up':
			axtemp.set(xlim=(x_min+xunit, x_max-xunit))
		elif event.button == 'down':
			axtemp.set(xlim=(x_min-xunit, x_max+xunit))
		fig.canvas.draw_idle()  # 绘图动作实时反映在图像上
	fig.canvas.mpl_connect('scroll_event', OnScroll)


def arr_change(close, window=1):
	ret = np.zeros(close.shape)
	ret[window:] = close[window:] / close[:-window] - 1
	ret[np.isnan(ret) | np.isinf(ret)] = 0
	return ret


def merge_pos(pos_old, pos_new, dateList):
	old_len = len(pos_old)
	dateList_len = len(dateList)
	if dateList_len - old_len > 20:
		print('大于20天，数据无法补齐。')
		return pos_new
	elif np.any(pos_old[-1,:] != pos_old[dateList_len-old_len-1,:]):
		print('数据不一致！')
		return pos_new
	pos_new[:old_len,:pos_old.shape[1]] = pos_old[:]
	return pos_new


def rolling_window(a, window_size):
	shape = (a.shape[0] - window_size + 1, window_size) + a.shape[1:]
	strides = (a.strides[0],) + a.strides
	return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def movsum(arr, window)->np.ndarray:
	ret = np.cumsum(arr, axis=0, dtype=float)
	ret[window:] = ret[window:] - ret[:-window]
	return ret


def movmean(arr, window)->np.ndarray:
	ret_movsum = movsum(arr, window)
	ret = ret_movsum / window
	return ret


def rebalance_one(holding):
	arr = np.copy(holding)
	arr[np.isnan(arr)] = 0
	rsum = np.sum(arr,1)
	rsum = rsum[:,np.newaxis]
	arr = arr / rsum
	arr[np.isnan(arr)|np.isinf(arr)] = 0
	return arr


def cross_idx(arr1:np.ndarray, arr2:np.ndarray):
	idx1 = arr1 < arr2
	idx2 = arr1 >= arr2
	idx3 = np.full(idx1.shape, False)
	idx3[1:] = idx1[:-1]
	idx = idx2 & idx3
	return idx


def load_validdata():
	# 有效交易日
	updownLimit_Path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "updownLimit.mat")
	updownLimit = hdf5storage.loadmat(updownLimit_Path)['updownLimit']
	tradingStatus_Path = os.path.join(GLOBAL_CONFIG['TwinDataRoot'], "tradingStatus.mat")
	tradingStatus = hdf5storage.loadmat(tradingStatus_Path)['tradingStatus']
	return updownLimit, tradingStatus


def validtrade(pos, updownLimit, tradingStatus):
	# 无效交易仓位清零，平衡给有效仓位
	mask = np.zeros(pos.shape[1], dtype=bool)
	for di in range(1,len(pos)):
		idx = np.where((np.abs(updownLimit[di,:])==1) | (tradingStatus[di,:]==2))
		mask[:] = False
		mask[idx] = True
		pos[di,mask] = pos[di-1,mask]
		sum_float = np.sum(pos[di,~mask])
		sum_fix = np.sum(pos[di,mask])
		if sum_float > 0:
			pos[di,~mask] = pos[di,~mask] / sum_float * (1 - sum_fix)
	return pos


def int2date(intdate):
	intyear = intdate // 10000
	intmonth = intdate % 10000 // 100
	intday = intdate % 100
	return datetime.date(intyear, intmonth, intday)


def date2int(dt_time):
	return 10000*dt_time.year + 100*dt_time.month + dt_time.day


def int2datestr(ndate):
	year = ndate // 10000
	month = (ndate % 10000) // 100
	day = ndate % 100
	sdate = f'{str(year)}-{str(month).rjust(2, "0")}-{str(day).rjust(2, "0")}'
	return sdate


def last_weekend(intdate):
	# return last saturday
	dt = int2date(intdate)
	idx = (dt.weekday() + 1) % 7
	sat = dt - datetime.timedelta(7+idx-6)
	return sat.year * 10000 + sat.month * 100 + sat.day


def last_monthend(intdate):
	# return last monthend
	dt = int2date(intdate)
	monthfirst = dt.replace(day=1)
	m_end = monthfirst - datetime.timedelta(days=1)
	return m_end.year * 10000 + m_end.month * 100 + m_end.day

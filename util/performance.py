import numpy as np


class Performance(object):
	def __init__(self, name, sharpe, ret, to, dd, ddlen, winpct, margin):
		self.name = name
		self.sharpe = sharpe
		self.ret = ret
		self.to = to
		self.dd = dd
		self.ddlen = ddlen
		self.winpct = winpct
		self.margin = margin

	def __str__(self):
		return '%6s%10.4f%10.4f%10.4f%10.2f%10.4f%10.0f%10.4f' % \
			   (self.name, self.sharpe, self.ret, self.to, self.margin, self.dd,
				self.ddlen, self.winpct)


def pnl(basedata, alpha, costRatio):
	len_alpha = len(alpha)
	absret_raw = np.zeros(len_alpha)
	absret_net = np.zeros(len_alpha)
	cost = np.zeros(len_alpha)
	nwin = np.zeros(len_alpha)
	nloss = np.zeros(len_alpha)
	turnover = np.zeros(len_alpha)

	basedata[np.isinf(basedata) | np.isnan(basedata)] = 0
	turnover[0] = np.sum(basedata[0, :])

	for di in range(2, len(alpha)):
		ret1d = basedata[di, :]
		absret_raw[di] = np.dot(alpha[di - 2, :], ret1d.T)
		turnover[di] = np.sum(np.abs(alpha[di - 1, :] - alpha[di - 2, :]))
		cost[di] = costRatio * turnover[di]
		absret_net[di] = absret_raw[di] - cost[di]

		fpnl = basedata[di - 2, :] * ret1d
		spnl = np.sign(fpnl)
		spnl_sum = sum(abs(spnl))
		spnl_diff = sum(spnl)
		nwin[di] = (spnl_sum + spnl_diff) / 2.0
		nloss[di] = (spnl_sum - spnl_diff) / 2.0

	return absret_raw, absret_net, cost, turnover, nwin, nloss


def pnl_ret(basedata, alpha, costRatio):
	# shp = alpha.shape
	# basedata = basedata[:shp[0], :shp[1]]

	len_alpha = len(alpha)
	absret_raw = np.zeros(len_alpha)
	absret_net = np.zeros(len_alpha)
	cost = np.zeros(len_alpha)
	turnover = np.zeros(len_alpha)

	basedata[np.isinf(basedata) | np.isnan(basedata)] = 0
	turnover[0] = np.sum(basedata[0, :])

	for di in range(2, len(alpha)):
		ret1d = basedata[di, :]
		absret_raw[di] = np.dot(alpha[di - 2, :], ret1d.T)
		turnover[di] = np.sum(np.abs(alpha[di - 1, :] - alpha[di - 2, :]))
		cost[di] = costRatio * turnover[di]
		absret_net[di] = absret_raw[di] - cost[di]

	return absret_net, cost, turnover


def piece_performance(absret, turnover, perf_name) -> Performance:
	sharpe = np.mean(absret) / np.std(absret)
	ret = np.sum(absret)
	to = np.mean(turnover)

	margin = 0
	to_sum = np.sum(turnover)
	if to_sum > 1e-9:
		margin = 10000 * np.sum(absret) / to_sum

	cumpnl = np.cumsum(absret)
	maxret = np.zeros(len(absret))
	maxret[0] = max(cumpnl[0], 0)
	for di in range(1, len(cumpnl)):
		maxret[di] = max(maxret[di - 1], cumpnl[di])

	drawdown = maxret - cumpnl
	dd = np.max(drawdown)

	len_cum = len(cumpnl)
	idx = np.where(drawdown == 0)
	pos = np.array(idx) + 1
	pos = np.append(pos, len_cum + 1)
	pos = np.insert(pos, 0, 0)
	dddiff = np.diff(pos)
	ddlen = np.max(dddiff) - 1

	winno = np.sum(absret > 0)
	losno = np.sum(absret < 0)

	if (winno + losno) < 0.5:
		winpct = 0.0
	else:
		winpct = winno / (winno + losno)

	perf = Performance(perf_name, sharpe, ret, to, dd, ddlen, winpct, margin)
	return perf


def year_idx(dateList, is_date, retlen):
	# Calc the begin and end for each year/month
	year = dateList // 10000
	iyear = np.zeros(len(dateList), dtype=int)
	iyear[0] = is_date
	count = 0
	for di in range(is_date + 1, retlen - 1):
		if year[di] != year[di + 1]:
			count += 1
			iyear[count] = di
	count += 1
	iyear[count] = retlen - 1
	iyear = iyear[:count + 1]
	return iyear


def print_year_performance(absret, turnover, dateList, is_date):
	# calc and output yearly/monthly peroformance
	iyear = year_idx(dateList, is_date, len(absret))

	print('%16s%10s%10s%10s%10s%10s%10s' % ('Sharpe', 'Return', 'TO', 'MARGIN', 'DD', 'DDLen', 'WinPct'))
	for yi in range(0, len(iyear) - 1):
		drng = range(iyear[yi] + 1, min(iyear[yi + 1] + 1, len(absret)))
		absret_piece = absret[drng]
		turnover_piece = turnover[drng]
		nyear = dateList[iyear[yi] + 1, 0] // 10000
		perf = piece_performance(absret_piece, turnover_piece, str(nyear))
		print(perf)

	perf = piece_performance(absret[is_date:], turnover[is_date:], 'ALL')
	print(perf)

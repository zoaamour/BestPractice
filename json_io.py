import os
import json
import pandas as pd

SCORE_CONFIG = {
	'Industry2UpLimit': {
		'MA': 3,
		'Interval': [0.0, 1, 2, 3, 4, 6, 100],
		'Weight': [-3.93, 2.93, 3.93, 12.5, 13.9, 29.71]
	},
	'Industry2UpLimitPCT': {
		'MA': 3,
		'Interval': [0, 0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 1],
		'Weight': [-4.79, -2.44, -2.38, -0.06, 3.93, 11.41, 12.4]
	},
	'Industry2DownLimit': {
		'MA': 3,
		'Interval': [0, 1, 2, 3, 4, 6, 10, 100],
		'Weight': [-1.79, -1.76, -9.09, -16.96, -6.27, -35.55, -44.57]
	},
	'Industry2DownLimitPCT': {
		'MA': 1,
		'Interval': [0, 0.005, 0.01, 0.02, 0.04, 0.1, 1],
		'Weight': [-1.3, -4.44, -4.48, -10, -10.25, -27.71]
	},
	'Industry2CloseToUpLimit': {
		'MA': 3,
		'Interval': [0.0, 1, 2, 3, 4, 100],
		'Weight': [-3.06, 2.4, 11.14, 11.75, 6.22]
	},
	'Industry2CloseToUpLimitPCT': {
		'MA': 3,
		'Interval': [0, 0.005, 0.02, 0.04, 0.06, 0.1, 1],
		'Weight': [-3.69, -0.48, 0.54, 3.75, 7.67, 9.99]
	},
	'Industry2-10DExcess': {
		'MA': 1,
		'Interval': [-1, -0.1, -0.08, -0.06, -0.04, -0.02, 0.0, 0.02, 0.04, 0.06, 0.08, 0.1, 1.0],
		'Weight': [4.95, -19.53, -22.08, -25.90, -21.48, -12.78, 2.97, 7.27, 13.23, 20.27, 35.31, 24.00]
	},
	'Industry2NewHigh': {
		'MA': 3,
		'Interval': [0.0, 1, 2, 3, 4, 6, 100],
		'Weight': [-4.19, 0.65, 3.85, 2.57, 6.87, 17.29]
	},
	'Industry2NewHighPCT': {
		'MA': 3,
		'Interval': [0.0, 0.02, 0.03, 0.04, 0.05, 0.06, 0.12, 0.18, 1],
		'Weight': [-4.33, -2.53, -1.97, 1.15, 3.43, 4.39, 11.09, 20.70]
	},
	'Industry2NewLow': {
		'MA': 3,
		'Interval': [0.0, 1, 2, 3, 4, 6, 10, 100],
		'Weight': [-0.36, -16.41, -15.7, -17.74, -18.38, -14.29, -2.22]
	},
	'Industry2NewLowPCT': {
		'MA': 3,
		'Interval': [0, 0.02, 0.03, 0.04, 0.05, 0.06, 0.12, 0.18, 1],
		'Weight': [0.15, -11.22, -19.13, -18.57, -22.39, -16.81, -15.77, -9.46]
	},
	# 'Industry2TOPctScore': {
	#     'MA': 2,
	#     'Interval': [-20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20],
	#     'Weight': [-9.54884,2.19444,3.66488,-12.6926,-10.9483,-12.4791,-11.6834,-13.5474,-11.0188,-21.2788]
	# },

}

Industry2UpLimit = [-0.0008, 0.0001, 0.0011, 0.0009, 0.0019, 0.0029]


def main():
	jpath = os.path.join('data', 'sw2factor.json')

	with open(jpath, 'w') as jfile:
		json.dump(SCORE_CONFIG, jfile, indent=4)

	with open(jpath, 'r', encoding="utf-8") as jfile:
		factors = json.load(jfile)

	print(SCORE_CONFIG==factors)

	weight = factors['Industry2UpLimit']['Weight']

	df = pd.DataFrame({1:Industry2UpLimit, 2:weight})
	corr = df[1].corr(df[2])



	pass


if __name__ == '__main__':
	main()

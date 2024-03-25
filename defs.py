#!/usr/bin/env python

import numpy as np

sources = {
	# 70x70
	'A1': { 'w': 70, 'h': 70, 'l': 3120, 'quality': 0 },
	'A2': { 'w': 70, 'h': 70, 'l': 3073, 'quality': 0 },
	'A3': { 'w': 70, 'h': 70, 'l': 3120, 'quality': 0 },
	'A4': { 'w': 70, 'h': 70, 'l': 3108, 'quality': 0 },

	# 80x40
	'B1': { 'w': 80, 'h': 40, 'l': 3145, 'quality': 0 },
	'B2': { 'w': 80, 'h': 40, 'l': 3100, 'quality': 0 },
	'B3': { 'w': 80, 'h': 40, 'l': 3115, 'quality': 0 },
	'B4': { 'w': 80, 'h': 40, 'l': 3125, 'quality': 0 },
	'B5': { 'w': 80, 'h': 40, 'l': 2708, 'quality': 0 },
	'B6': { 'w': 80, 'h': 40, 'l': 2700, 'quality': 0 },
	'B7': { 'w': 80, 'h': 40, 'l': 1398, 'quality': 0 },
	'B8': { 'w': 80, 'h': 40, 'l': 1388, 'quality': 0 },

	# 40x40
	'C1': { 'w': 40, 'h': 40, 'l': 2755, 'quality': 0 },
	'C2': { 'w': 40, 'h': 40, 'l': 2700, 'quality': 0 },
	'C3': { 'w': 40, 'h': 40, 'l': 2727, 'quality': 0 },
	'C4': { 'w': 40, 'h': 40, 'l': 2687, 'quality': 0 },
	'C5': { 'w': 40, 'h': 40, 'l': 2742, 'quality': 0 },
	'C6': { 'w': 40, 'h': 40, 'l': 1398, 'quality': 0 },
	'C7': { 'w': 40, 'h': 40, 'l': 1400, 'quality': 0 },
	'C8': { 'w': 40, 'h': 40, 'l': 1400, 'quality': 0 },
	'C7': { 'w': 40, 'h': 40, 'l': 1388, 'quality': 0 },
	'C8': { 'w': 40, 'h': 40, 'l': 1405, 'quality': 0 }
}

w = 1320 # measured
l = 2430 # measured
h = 2390 # measured

h_A1 = 10 # calc
h_A2 = 10 # calc
h_A3 = 30 # calc
h_A4 = 30 # calc

l_win = 1300 # measured
l_s = 500 # defined
w_s = 500 # defined
h_s = 500 # defined

h_S1 = 20 # calc
h_S2 = 20 # calc
h_S3 = 20 # calc
h_S4 = 20 # calc

h_R = 400 # defined
l_R = l - 2 * h_R # calc

# l_R = 
# h_R = (l - l_R) / 2


x_1A = 50 # defined
x_1B = 40 # defined
x_1 = x_1A + x_1B


parts = {
	# A's
	'A1': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A1) }
	},
	'A2': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A2) }
	},
	'A3': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A3) }
	},
	'A4': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A4) }
	},

	# B's
	'B_1_3': {
		'num': 2,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'B_2_4': {
		'num': 2,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': l }
	},

	# F
	'F_1_2': {
		'num': 2,
		'quality': 2,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},

	# S's
	'SF_1': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 40, 'h': 80, 'l': (l_win - 2 * x_1) }
	},
	'SF_2': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 40, 'h': 80, 'l': (l_s - 2 * x_1) }
	},

	'SD_1_2': {
		'num': 2,
		'quality': 1,
		'size': { 'w': 40, 'h': 40, 'l': ( (l_s - 2 * x_1) * np.sqrt(2) ) }
	},

	'SA_1': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S1) }
	},
	'SA_2': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S2) }
	},
	'SA_3': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S3) }
	},
	'SA_4': {
		'num': 1,
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S4) }
	},

	'S_1': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': l_win }
	},
	'S_2': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': l_win }
	},
	'S_3': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': l_s }
	},
	'S_4': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': w_s }
	},
	'S_5': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'S_6': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'S_7': {
		'num': 1,
		'quality': 0,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},

	# R's
	'R_1': {
		'num': 4,
		'quality': 0,
		'size': { 'w': 40, 'h': 40, 'l': w }
	},
	'R_2': {
		'num': 4,
		'quality': 0,
		'size': { 'w': 40, 'h': 40, 'l': l_R }
	},
	'R_3': {
		'num': 8,
		'quality': 0,
		'size': { 'w': 40, 'h': 40, 'l': (h_R * np.sqrt(2) ) }
	},
	'R_4': {
		'num': 4,
		'quality': 0,
		'size': { 'w': 40, 'h': 40, 'l': (h_R - 40) }
	},

	# D's
	'D_1': {
		'num': 4*3,
		'quality': 1,
		'size': { 'w': 40, 'h': 40, 'l': (h_R * np.sqrt(2) ) } # same as R_3?
	},

}
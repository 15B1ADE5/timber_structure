#!/usr/bin/env python

# import floor
import numpy as np

sources = {
	# 70x70
	'A1': { 'size': { 'w': 70, 'h': 70, 'l': 3120 }, 'quality': 0 },
	'A2': { 'size': { 'w': 70, 'h': 70, 'l': 3073 }, 'quality': 0 },
	'A3': { 'size': { 'w': 70, 'h': 70, 'l': 3120 }, 'quality': 0 },
	'A4': { 'size': { 'w': 70, 'h': 70, 'l': 3108 }, 'quality': 0 },

	# 80x40
	'B1': { 'size': { 'w': 40, 'h': 80, 'l': 3145 }, 'quality': 0 },
	'B2': { 'size': { 'w': 40, 'h': 80, 'l': 3100 }, 'quality': 0 },
	'B3': { 'size': { 'w': 40, 'h': 80, 'l': 3115 }, 'quality': 0 },
	'B4': { 'size': { 'w': 40, 'h': 80, 'l': 3125 }, 'quality': 0 },
	'B5': { 'size': { 'w': 40, 'h': 80, 'l': 2708 }, 'quality': 0 },
	'B6': { 'size': { 'w': 40, 'h': 80, 'l': 2700 }, 'quality': 0 },
	'B7': { 'size': { 'w': 40, 'h': 80, 'l': 1398 }, 'quality': 0 },
	'B8': { 'size': { 'w': 40, 'h': 80, 'l': 1388 }, 'quality': 0 },

	# 40x40
	'C1': { 'size': { 'w': 40, 'h': 40, 'l': 2755 }, 'quality': 0 },
	'C2': { 'size': { 'w': 40, 'h': 40, 'l': 2700 }, 'quality': 0 },
	'C3': { 'size': { 'w': 40, 'h': 40, 'l': 2727 }, 'quality': 0 },
	'C4': { 'size': { 'w': 40, 'h': 40, 'l': 2687 }, 'quality': 0 },
	'C5': { 'size': { 'w': 40, 'h': 40, 'l': 2742 }, 'quality': 0 },
	'C6': { 'size': { 'w': 40, 'h': 40, 'l': 1398 }, 'quality': 0 },
	'C7': { 'size': { 'w': 40, 'h': 40, 'l': 1400 }, 'quality': 0 },
	'C8': { 'size': { 'w': 40, 'h': 40, 'l': 1400 }, 'quality': 0 },
	'C7': { 'size': { 'w': 40, 'h': 40, 'l': 1388 }, 'quality': 0 },
	'C8': { 'size': { 'w': 40, 'h': 40, 'l': 1405 }, 'quality': 0 }
}

print('###### DEFS ######')
# Measures / defines:
w = 1310 # measured
l = 2380 # measured
h = 2330 # measured

w_F = 300 # defined / measured

d = 350 # defined

# For floor curvature compensation
# hf_0 = 40
# hf_l_l = 1000
# hf_l_h = 90
# hf_w_w = 1000
# hf_w_h = 70

l_win = 1000 # measured
l_s = 600 # defined
w_s = 400 # defined
h_s = 500 # defined

h_R = 440 # defined / measured
l_R = None # if None -> to be calculated

x_1A = 50 # defined
x_1B = 40 # defined

# floorCC = floor.CurvatureCompensator(
# 	hf_0,
# 	hf_l_l,
# 	hf_l_h,
# 	hf_w_w,
# 	hf_w_h
# )
# print('Floor Curvature Compensation:')
# print(f' - Floor angle l: {np.degrees( floorCC.angle_l() ):.1f} o')
# print(f' - Floor angle w: {np.degrees( floorCC.angle_w() ):.1f} o')

h_A1 = 0
h_A2 = 0
h_A3 = 0
h_A4 = 0

h_S1 = 0 # calc
h_S2 = 0 # calc
h_S3 = 0 # calc
h_S4 = 0 # calc

if l_R is None:
	l_R = round(l - 2 * h_R) # calc
elif h_R is None:
	h_R = (l - l_R) / 2


x_1 = x_1A + x_1B


part_base = {
	'size': { 'w': 0, 'h': 0, 'l': 0 },
	'num': 1
}

parts = {
	# A's
	'A1': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A1-40) }
	},
	'A2': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A2-40) }
	},
	'A3': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A3-40) }
	},
	'A4': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A4-40) }
	},

	# B's
	'B_1_3': {
		'num': 2,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'B_2_4': {
		'num': 2,
		'size': { 'w': 40, 'h': 80, 'l': l }
	},

	# F
	'F_1_2_3_4': {
		'num': 4,
		'size': { 'w': 40, 'h': 80, 'l': w_F }
	},

	# S's
	'SF_1': {
		'num': 0,
		'size': { 'w': 40, 'h': 80, 'l': round(l_win - 2 * x_1) }
	},
	'SF_2': {
		'num': 0,
		'size': { 'w': 40, 'h': 80, 'l': round(l_s - 2 * x_1) }
	},

	'SD_1_2': {
		'num': 0,
		'size': {
			'w': 40, 'h': 40,
			'l': 300
			# 'l': round( (l_s - 2 * x_1) * np.sqrt(2) )
		}
	},

	'SA_1': {
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S1) }
	},
	'SA_2': {
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S2) }
	},
	'SA_3': {
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S3) }
	},
	'SA_4': {
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S4) }
	},

	'S_1': {
		'size': { 'w': 40, 'h': 80, 'l': l_win }
	},
	'S_2': {
		'size': { 'w': 40, 'h': 80, 'l': l_win }
	},
	'S_3': {
		'size': { 'w': 40, 'h': 80, 'l': l_s }
	},
	'S_4': {
		'size': { 'w': 40, 'h': 80, 'l': w_s }
	},
	'S_5': {
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'S_6': {
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'S_7': {
		'size': { 'w': 40, 'h': 80, 'l': w }
	},

	# R's
	'R_w': {
		'num': 2,
		'size': { 'w': 40, 'h': 40, 'l': w }
	},
	'R_l': {
		'num': 1,
		'size': { 'w': 40, 'h': 40, 'l': l_R }
	},
	'R_l_back': {
		'num': 1,
		'size': { 'w': 40, 'h': 80, 'l': l_R }
	},
	'R_dl': {
		'num': 4,
		'size': { 'w': 40, 'h': 40, 'l': round(h_R * np.sqrt(2) ) }
	},
	'R_dw': {
		'num': 0,
		'size': { 'w': 40, 'h': 40, 'l': d }
	},
	'R_h': {
		'num': 4,
		'size': { 'w': 40, 'h': 40, 'l': (h_R - 40) }
	},

	# D's
	'D_1': {
		'num': 4*3,
		'size': { 'w': 40, 'h': 40, 'l': d }
	},

	'H_1': {
		'num': 1,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},
	'H_2-5': {
		'num': 3,
		'size': { 'w': 40, 'h': 40, 'l': w }
	},
}

for part in parts:
	parts[part] = part_base | parts[part]

for part in sources:
	sources[part] = part_base | sources[part]

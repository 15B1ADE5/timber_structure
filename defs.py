#!/usr/bin/env python

import floor
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
w = 1320 # measured
l = 2430 # measured
h = 2390 # measured

# For floor curvature compensation
hf_0 = 40
hf_l_l = 1000
hf_l_h = 90
hf_w_w = 1000
hf_w_h = 70

l_win = 1300 # measured
l_s = 500 # defined
w_s = 500 # defined
h_s = 500 # defined

h_R = 400 # defined
l_R = None

x_1A = 50 # defined
x_1B = 40 # defined

floorCC = floor.CurvatureCompensator(
	hf_0,
	hf_l_l,
	hf_l_h,
	hf_w_w,
	hf_w_h
)
print('Floor Curvature Compensation:')
print(f' - Floor angle l: {np.degrees( floorCC.angle_l() ):.1f} o')
print(f' - Floor angle w: {np.degrees( floorCC.angle_w() ):.1f} o')

h_A1 = floorCC.compensated_h(80, 80)
h_A2 = 10 # calc
h_A3 = 30 # calc
h_A4 = 30 # calc

h_S1 = 20 # calc
h_S2 = 20 # calc
h_S3 = 20 # calc
h_S4 = 20 # calc

if l_R is None:
	l_R = round(l - 2 * h_R) # calc
elif h_R is None:
	h_R = (l - l_R) / 2

x_1 = x_1A + x_1B


part_base = {
	'size': { 'w': 0, 'h': 0, 'l': 0 },
	'num': 1,
	'quality': 0
}

parts = {
	# A's
	'A1': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A1) }
	},
	'A2': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A2) }
	},
	'A3': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A3) }
	},
	'A4': {
		'size': { 'w': 70, 'h': 70, 'l': (h+h_A4) }
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
	'F_1_2': {
		'num': 2,
		'quality': 2,
		'size': { 'w': 40, 'h': 80, 'l': w }
	},

	# S's
	'SF_1': {
		'quality': 1,
		'size': { 'w': 40, 'h': 80, 'l': round(l_win - 2 * x_1) }
	},
	'SF_2': {
		'quality': 1,
		'size': { 'w': 40, 'h': 80, 'l': round(l_s - 2 * x_1) }
	},

	'SD_1_2': {
		'num': 2,
		'quality': 1,
		'size': { 'w': 40, 'h': 40, 'l': round( (l_s - 2 * x_1) * np.sqrt(2) ) }
	},

	'SA_1': {
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S1) }
	},
	'SA_2': {
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S2) }
	},
	'SA_3': {
		'quality': 1,
		'size': { 'w': 70, 'h': 70, 'l': (h_s + h_S3) }
	},
	'SA_4': {
		'quality': 1,
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
	'R_1': {
		'num': 2,
		'size': { 'w': 40, 'h': 40, 'l': w }
	},
	'R_2': {
		'num': 1,
		'size': { 'w': 40, 'h': 40, 'l': l_R }
	},
	'R_3': {
		'num': 0,
		'size': { 'w': 40, 'h': 40, 'l': round(h_R * np.sqrt(2) ) }
	},
	'R_4': {
		'num': 4,
		'size': { 'w': 40, 'h': 40, 'l': (h_R - 40) }
	},

	# D's
	'D_1': {
		'num': 4*3,
		'quality': 1,
		'size': { 'w': 40, 'h': 40, 'l': 350 } # same as R_3?
	},

	'H_1_5': {
		'num': 5,
		'quality': 1,
		'size': { 'w': 40, 'h': 40, 'l': w } # same as R_3?
	},
}

for part in parts:
	parts[part] = part_base | parts[part]

for part in sources:
	sources[part] = part_base | sources[part]

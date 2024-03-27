import numpy as np

#.___l____.
# \a      |
#  \      |
#   \     |
#    c    h
#     \   |
#      \  |
#       \b|
#        \|
#         '
       
class CurvatureCompensator:
	def __init__(
		self, 
		hf_0,
		hf_l_l,
		hf_l_h,
		hf_w_w,
		hf_w_h
	):
		hf_l_l -= hf_0
		hf_l_h -= hf_0
		hf_w_w -= hf_0
		hf_w_h -= hf_0
		self.tanA_l = hf_l_h / hf_l_l
		self.tanA_w = hf_w_h / hf_w_w
	
	def angle_l(self):
		return np.arctan(self.tanA_l)

	def angle_w(self):
		return np.arctan(self.tanA_w)

	def compensated_h(self, l, w):
		return l * self.tanA_l + w * self.tanA_w
#!/usr/bin/env python

import defs
import yaml
import numpy as np

def classify_by_WH(parts):
	part_classes = {}
	for part in parts:
		if (parts[part]['size']['w'], parts[part]['size']['h']) in part_classes:
			part_classes[ (parts[part]['size']['w'], parts[part]['size']['h']) ][part] = parts[part]
		else:
			part_classes[ (parts[part]['size']['w'], parts[part]['size']['h']) ] = { part: parts[part] }
	return part_classes


def parts_to_lengths(parts):
	out = []
	for part in parts:
		for _ in range(parts[part]['num']):
			out.append( (parts[part]['size']['l'], part) )
	return out

def solve_bin_problem(bins, items):
	items = sorted(items, reverse=True)
	bins = sorted(bins)
	
	items_left = []
	packed_bins = {}
	for bin_ in bins:
		packed_bins[bin_] = []

	for item in items:
		best_bin = None
		best_remaining_capacity = float('inf')

		for bin_ in packed_bins:
			capacity_left = bin_[0] - sum([size for size, _ in packed_bins[bin_]])
			
			if item[0] <= capacity_left:
				capacity_left -= item[0]
				if capacity_left < best_remaining_capacity:
					best_bin = bin_
					best_remaining_capacity = capacity_left
		
		if best_bin:
			packed_bins[best_bin].append(item)
		else:
			items_left.append(item)

	return (packed_bins, items_left)

def print_packed(sources):
	for source in sources:
		capacity_left = source[0] - sum([size for size, _ in sources[source]])
		print(f'   {source[1]} (size: {source[0]} / left: {capacity_left}):')
		for item in sources[source]:
			print(f'      {item[1]} (size: {item[0]})')

sources = classify_by_WH(defs.sources)
parts = classify_by_WH(defs.parts)


for class_ in parts:
	print(f'--- {class_} ---')
	packed_bins, items_left = solve_bin_problem(
		parts_to_lengths(sources[class_]),
		parts_to_lengths(parts[class_])
	)

	print('Packed:')
	print_packed(packed_bins)
	left = sum([size for size, _ in items_left])
	print(f'Left ({left}):')
	for item in items_left:
		print(f'   {item[1]} (size: {item[0]})')

# print(parts_to_lengths(sources[(40,40)]) )
#!/usr/bin/env python

import defs
import json
import numpy as np

def parts_to_lengths(parts):
	out = []
	for part in parts:
		out.extend( [ parts[part]['size']['l'] for _ in range(parts[part]['num']) ] )
	return out

# def best_fit(parts, sources)

print( parts_to_lengths(defs.parts) )
print((json.dumps(defs.parts, indent = 4)))
import sys
import time

sys.path.insert(0, '/home/uas/Documents/blue/env/XPlaneConnect/Python3/src')

import xpc

uas = xpc.XPlaneConnect()



for i in range(10):
	pose = uas.getPOSI()
	print(pose)

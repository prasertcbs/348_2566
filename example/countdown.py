import time
import random

def v1():
	for i in range(10, -1, -1):
		print(i, end=" ") # flush=False
	print()

def v2():
	for i in range(10, -1, -1):
		# print(i, end=" ", flush=False) # default flush = False
		print(i, end=" ", flush=True)
		time.sleep(.1)
	print()

if __name__ == '__main__':
	v2()

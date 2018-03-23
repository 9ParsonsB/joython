#!/usr/bin/env python2
def calc(a,b,c,d):
  for x in range(a,b):
	print "\touter " + str(x)
	for y in range(c,d):
		print "\t\tinner " + str(y)

calc(3,7,4,10)
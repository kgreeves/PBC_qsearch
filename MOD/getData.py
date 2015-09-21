#!/usr/bin/env python

from numpy import loadtxt
from math import ceil

def getData(filename,datatype):
	coords = [];
	if int(datatype) == 1 : # atom, X, Y, Z
		j=0;
		file = open(filename, 'r');
		for line in file:
			j+=1;
			coords.append(line.split());
		file.close();
	else : # Charge Data
		j=0;
		file = open(filename, 'r');
		for line in file:
			j+=1;
			coords.append(line.split());
		file.close();
	return coords;

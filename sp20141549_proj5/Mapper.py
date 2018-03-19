#!/usr/bin/python
#-*- coding: utf-8 -*-

from sys import stdin, stdout

while True:
	str1 = stdin.readline().strip()       # input the data

	if str1 == "":
		break
	lis = str1.split()					  # split data
	for i in range(0, len(lis)-1):		  # print the result
		stdout.write(lis[i]+' ' + lis[i+1] + "\t" + str(1) + "\n")

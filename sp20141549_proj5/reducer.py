#!/usr/bin/python

from sys import stdin, stdout

dic = {}		# dictionary for store 
while True:
	str1 = stdin.readline().strip() # input the data
	if str1 == "":
		break

	word, cnt = str1.split('\t')    # split the words and counts
	if( word in dic ):
		dic[word] +=  int(cnt)
	else:
		dic[word] = int(cnt)
keys = dic.keys()
keys.sort()
for i in keys:						# print the result
	stdout.write(i+"\t"+str(dic[i])+"\n")


#!/usr/bin/python  
#-*- coding: utf-8 -*-

import requests							#import libraries.
from bs4 import BeautifulSoup

visited = []							# visited url in list.

cnt = 0									# set count variable.
in_url = "http://cspro.sogang.ac.kr/~gr120160213/index.html"

"""
	Name	  : crawling
	Parameter : url		- input url.
				visited - Check for visited url for this list.
	Object    : Set root page url, then search all pages linked with hyperlink and crawl texts.
	return	  : None 
"""


def crawling(url, visited):
	global cnt
	if url in visited:					# check url in list visited.
		return
	else:
		try:							# use try for is it valid.
			req = requests.get(url)

			if req.ok == False:
				return

			soup = BeautifulSoup(req.content,"html.parser")
			visited.append(url)

			out_name = "Output_"+ "%04d" %cnt + ".txt"
			# file open.
			f_out = open(out_name, "wt")
			# write file.
			f_out.writelines(soup.get_text())
			# file close.
			f_out.close()
			cnt +=1
					# search for a tag.
			for i in soup.find_all('a'):
				s = str(i)				 # none type to string type.
				s = i.get('href')	

				if( s != "" and '?' not in s and '#' not in s ):			# check link is valid.
					if( s.find( "http://cspro.sogang.ac.kr/~gr120160213/") == -1 ):
						s = "http://cspro.sogang.ac.kr/~gr120160213/" + s
					
					crawling(s,visited)										# call function reculsive.

		except:
			pass

crawling(in_url,visited)						# call function.
outfile = open("URL.txt","w")

for i in range(cnt ):							# print out url data to URL.txt.
	outfile.writelines(visited[i] + '\n')

outfile.close()									# close file.








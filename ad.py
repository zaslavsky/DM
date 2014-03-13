#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  spider.py
#  
#  Copyright 2014 zaslavsky <zaslavsky@CELESTIA>
#  

import mechanize
from BeautifulSoup import BeautifulSoup
import pymongo




browse = mechanize.Browser()

url_home = "http://ru.dotabuff.com" 	     	


def def_open_url(url): 							
	open_url = browse.open(url)
	read_text = open_url.read()
	soup = BeautifulSoup(read_text)
	print soup								

def main():
	def_open_url(url_home)

if __name__ == '__main__':
	main()

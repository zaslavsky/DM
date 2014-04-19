#!/usr/bin/env python
#-*- encoding: cp1251 -*-

import json, urllib, xlwr, xlrd


url_main = "http://api.worldoftanks.ru/wot/encyclopedia/tankinfo/?application_id=09be322fee8ba81d502df3cd5a03a6c5"








txt_data = urllib.urlopen(url_main+"&tank_id=81").read()

data = json.loads(txt_data)

print data["data"]["81"]["weight"]

def main():
	
	return 0




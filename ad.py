#!/usr/bin/env python
#-*- encoding: cp1251 -*-

import json, urllib, xlrd, xlwt


file_data = xlwt.Workbook().add_sheet('Main')

url_main = "http://api.worldoftanks.ru/wot/encyclopedia/tankinfo/?application_id=09be322fee8ba81d502df3cd5a03a6c5"

txt_data = urllib.urlopen(url_main+"&tank_id=1").read()

data = json.loads(txt_data)

print data["data"]["1"]["weight"]


def data_save():
	
	file_data.write(0, 0, 'Player')
	file_data.write(1, 0, 7)
	#ws.write(2, 2, xlwt.Formula("A3+B3"))
	
	file_data.save('data.xls')

data_save()
	

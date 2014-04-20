#!/usr/bin/env python
#-*- encoding: cp1251 -*-

import json, urllib, xlrd, xlwt, time
from xlutils.copy import copy

localdata=xlwt.Workbook()
file_data=localdata.add_sheet('Main')


source_filename = "mask.xls"
destination_filename = "data.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)  # Открываем исходный документ
read_sheet = read_book.get_sheet(0)  # Читаем из первого листа
localdata = copy(read_book)  # Копируем таблицу в память, в неё мы ниже будем записывать
ws = localdata.get_sheet(0)  # Будем записывать в первый лист



APP_ID="09be322fee8ba81d502df3cd5a03a6c5"

url_info = "http://api.worldoftanks.ru/wot/encyclopedia/tankinfo/?application_id="+APP_ID 
url_user_tanks = "http://api.worldoftanks.ru/wot/tanks/stats/?application_id="+APP_ID
url_stats = "http://api.worldoftanks.ru/wot/account/info/?application_id="+APP_ID
profile="&account_id="

I=1680926
ID=1680898
ID=I

URL=url_stats+profile+str(ID)
data = json.loads(urllib.urlopen(URL).read())

player_stat=data["data"][str(ID)]["statistics"]["all"]

games=player_stat["battles"]
wins=player_stat["wins"]

def data_grabbing():
	while True:
		txt_data = urllib.urlopen(url_stat+profile+str(ID)).read()
		data = json.loads(txt_data)
		try:print len(data["data"][str(ID)])
		except: print("No player: " +str(ID))
		ID-=1
		time.sleep(0.5)


def data_save():
	
	ws.write(1, 0, str(ID))
	ws.write(1, 1,  str(games))
	ws.write(1, 2,  str(wins))
	#ws.write(2, 2, xlwt.Formula("A3+B3"))
	
	localdata.save(destination_filename)
	
data_save()

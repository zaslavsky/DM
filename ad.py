#!/usr/bin/env python
#-*- encoding: cp1251 -*-
from init import *

localdata=xlwt.Workbook()
file_data=localdata.add_sheet('Main')

client = pymongo.MongoClient("localhost", 27017)
db=client.WOT
db.players
#db.players.save()


source_filename = "mask.xls"
destination_filename = "data.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)  # Открываем исходный документ
read_sheet = read_book.get_sheet(0)  # Читаем из первого листа
localdata = copy(read_book)  # Копируем таблицу в память, в неё мы ниже будем записывать
xls = localdata.get_sheet(0)  # Будем записывать в первый лист

URL=url_stats+profile+str(ID)
nojson=urllib.urlopen(URL).read()
data = json.loads(urllib.urlopen(URL).read())

player_stat=data["data"][str(ID)]["statistics"]["all"]

games=player_stat["battles"]
wins=player_stat["wins"]

print games,wins
#print data
#print "\n\n\n\n"+str(nojson)
db.players.save(data)

#player_stat=a["data"][str(ID)]["statistics"]["all"]

#games=player_stat["battles"]
#wins=player_stat["wins"]

def data_grabbing():
	while True:
		txt_data = urllib.urlopen(url_stat+profile+str(ID)).read()
		data = json.loads(txt_data)
		try:
			print len(data["data"][str(ID)])
			print "battles:"+str(player_stat["battles"])
			print "battles:"+str(player_stat["wins"])
		
		except: print("No player: " +str(ID))
		ID-=1
		time.sleep(0.5)


def data_save():
	
	xls.write(1, 0, str(ID))
	xls.write(1, 1,  str(games))
	xls.write(1, 2,  str(wins))
	#xls.write(2, 2, xlwt.Formula("A3+B3"))
	
	localdata.save(destination_filename)
	
#data_save()


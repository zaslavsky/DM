#!/usr/bin/env python
#-*- encoding: cp1251 -*-
from init import *



client = pymongo.MongoClient("localhost", 27017)
db=client.WOT
db.players

BORDER=5000
ID=1680920

def data_stat_get(ID):
	URL=url_stats+profile+str(ID)
	text_json=urllib.urlopen(URL).read()
	data = json.loads(text_json)
	data=data["data"][str(ID)]
	
	try: data_stat=data["statistics"]["all"]
	except: 
		print("No Player")
		return 0
	if data_stat["battles"]<BORDER:
		print("To low")
		return 0
		 
	return data
	
def data_tanks_get(ID):
	URL=url_user_tanks+profile+str(ID)
	text_json=urllib.urlopen(URL).read()
	data = json.loads(text_json)
	data=data["data"][str(ID)]
	return data

def dbsave(ID,nick,data,tanks):
	db.players.save({"_id":ID ,"nick":nick, "data":data, "tanks":tanks})
	
def data_download():
	Id=ID
	while True:
		data=data_stat_get(Id)
		if data==0:pass
		else:
			tanks=data_tanks_get(Id)
			dbsave(Id,data["nickname"],data["statistics"]["all"],tanks)
		Id+=1
		#time.sleep(0.1)
		
def data_xlxfill():
	docs = list(db.players.find())
	file_players.write(0, 0, 'ID')
	file_players.write(0, 1, 'Nick')
	file_players.write(0, 2, 'battles')
	file_players.write(0, 3, 'wins')
	file_players.write(0, 4, 'losses')
	file_players.write(0, 5, 'draws')
	file_players.write(0, 6, 'shots')
	file_players.write(0, 7, 'hits')
	file_players.write(0, 8, 'hits percents')
	file_players.write(0, 9, 'KILLS')
	file_players.write(0, 10, 'Winrate')
	file_players.write(0, 11, 'Survive')
	#file_players.write(0, 9, 'tanks played')
	count=0
	print docs[0]["data"].keys()
	while count!=len(docs):
		index=count+1
		tank_count=len(docs[count]["tanks"])
		docs[count]["data"]["wins"]
		base=float(docs[count]["data"]["battles"])
		winrate=(docs[count]["data"]["wins"]/base)*100
		survived=(docs[count]["data"]["survived_battles"]/base)*100
		file_players.write(index, 0, docs[count]["_id"])
		file_players.write(index, 1, docs[count]["nick"])
		file_players.write(index, 2, docs[count]["data"]["battles"])
		file_players.write(index, 3, docs[count]["data"]["wins"])
		file_players.write(index, 4, docs[count]["data"]["losses"])
		file_players.write(index, 5, docs[count]["data"]["draws"])
		file_players.write(index, 6, docs[count]["data"]["shots"])
		file_players.write(index, 7, docs[count]["data"]["hits"])
		file_players.write(index, 8, docs[count]["data"]["hits_percents"])
		file_players.write(index, 9, docs[count]["data"]["frags"])
		file_players.write(index, 10, int(winrate))
		file_players.write(index, 11, int(survived))
		#file_players.write(index, 9, tank_count)
		#file_players.write(index, 6, docs[index]["data"][""])
		count+=1
	xls.save('data.xls')
		
 	
 	
	
def tanks_list():
	URL=url_tanks_list+profile
	text_json=urllib.urlopen(URL).read()
	data = json.loads(text_json)
	data=data["data"]
	return data.keys()

data_xlxfill()
#
#tanks_list()
#data_download()
#docs = list(db.players.find({"_id":1680926}))
#print docs[0]["data"].keys()

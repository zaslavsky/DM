#!/usr/bin/env python
#-*- encoding: cp1251 -*-
from init import *

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
	count=0
	Id=ID
	while True:
		data=data_stat_get(Id)
		if data==0:pass
		else:
			count+=1
			tanks=data_tanks_get(Id)
			dbsave(Id,data["nickname"],data["statistics"]["all"],tanks)
		Id+=1
		print count
		#time.sleep(0.1)
		
def form():
	file_tanks.write(0, 0, 'Nick')
	file_tanks.write(0, 1, 'Nation')
	file_tanks.write(0, 2, 'Tank')
	file_tanks.write(0, 3, 'Type')
	file_tanks.write(0, 4, 'battles')
	file_tanks.write(0, 5, 'Wins')
	file_tanks.write(0, 6, 'spotted')
	file_tanks.write(0, 7, 'shoots')
	file_tanks.write(0, 8, 'frags')
	file_tanks.write(0, 9, 'Damage_dealth')
	file_tanks.write(0, 10, 'Damage_recive')
	file_tanks.write(0, 11, 'Survive')
	
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
		winrate=int(winrate)
		survived=(docs[count]["data"]["survived_battles"]/base)*100
		survived=int(survived)
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
		file_players.write(index, 10, str(winrate)+"%")
		file_players.write(index, 11, str(survived)+"%")
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

#data_xlxfill()
#
#tanks_list()
#data_download()
#docs = list(db.players.find({"_id":MY_ID}))
#for p in range(len(docs)):
#	for i in range(len(docs[p]["tanks"])):
#		tankid= str(docs[p]["tanks"][i]["tank_id"])
#		tankname=tanklib[tankid]["name"]
#		sep=tankname.find(":")+1
#		if tankname[sep:]=="GAZ-74b":print "lol"
		
		
#		file_tanks.write(0,)
		
def data_tanks_xlxfill():
	raw=1
	docs = list(db.players.find())
	#docs = list(db.players.find({"_id":MY_ID}))
	tanks=tanklib.keys()
	form()
	for user in range(len(docs)):
		u_tanks=docs[user]["tanks"]
		for tank in range(len(u_tanks)):
			tank_id=u_tanks[tank]["tank_id"]
			t_name=tanklib[str(tank_id)]["name"]
			t_type=tanklib[str(tank_id)]["type"]
			name_split=t_name.find(":")+1
			nat_split=t_name.find("_")
			file_tanks.write(raw, 0, docs[user]["nick"])
			file_tanks.write(raw, 1, t_name[1:nat_split])
			file_tanks.write(raw, 2, t_name[name_split:])
			file_tanks.write(raw, 3, t_type)
			file_tanks.write(raw, 4, u_tanks[tank]["all"]["battles"])
			file_tanks.write(raw, 5, u_tanks[tank]["all"]["wins"])
			file_tanks.write(raw, 6, u_tanks[tank]["all"]["spotted"])
			file_tanks.write(raw, 7, u_tanks[tank]["all"]["shots"])
			file_tanks.write(raw, 8, u_tanks[tank]["all"]["frags"])
			file_tanks.write(raw, 9, u_tanks[tank]["all"]["damage_dealt"])
			file_tanks.write(raw, 10, u_tanks[tank]["all"]["damage_received"])
			file_tanks.write(raw, 11, u_tanks[tank]["all"]["survived_battles"])
			raw+=1
	xls.save('data.xls')
		
	
data_tanks_xlxfill()
#print tank
#for i in docs:
#	for a in range(len(i["tanks"])):
#		tid=str(i["tanks"][a]["tank_id"])
#		print str(i["tanks"][a]["all"]["spotted"])+" by "+str(tanklib[tid]["name"])#.keys()

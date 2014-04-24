#!/usr/bin/env python
#-*- encoding: cp1251 -*-
from init import *



client = pymongo.MongoClient("localhost", 27017)
db=client.WOT
db.players
#db.players.save()

BORDER=100
ID=1680920

def data_stat_get(ID):
	URL=url_stats+profile+str(ID)
	text_json=urllib.urlopen(URL).read()
	data = json.loads(text_json)
	
	data=data["data"][str(ID)]#["statistics"]["all"]
	
	try: data_stat=data["statistics"]["all"]
	except: 
		print("No Player")
		return 0
	if data_stat["battles"]<BORDER:
		print("To low")
		return 0
		
	games=data_stat["battles"]
	wins=data_stat["wins"]
	losses=data_stat["losses"]
	draws=data_stat["draws"]
	spotted=["spotted"]
	shoots=data_stat["shots"]
	hits_percents=data_stat["hits_percents"]
	
	damage_dealt=data_stat["damage_dealt"]
	damage_recive=data_stat["damage_received"]
	
	frags=data_stat["frags"]
	survive=data_stat["survived_battles"]
	
	battle_avg_xp=data_stat["battle_avg_xp"]
	
	nick=data["nickname"]

	print nick
	print str(ID)+" games:"+str(games)
	#print games
	print "Wins:" +str(wins)
	print "Draws: " +str(draws)
	print "Frags: "+str(frags)
	
def dbgs(ID):
	URL=url_stats+profile+str(ID)
	text_json=urllib.urlopen(URL).read()
	data = json.loads(text_json)
	data=data["data"][str(ID)]["statistics"]["all"]["shots"]
	db.users.save({"_id":ID , "data":{"games":23, "wins":20} })
	#for user in db.users.find():
#		print user
	#users = db.players.find({data: {"$exists": 1}}, {"data.1680920.statistics.all": true}).pretty()
	print data

	
	print data
#db.users.save({"_id":1680926 , "data":{"games":23, "wins":20} })
user=db.user.find({ "_id" : 1880926 })
user=json.loads(user)
print user
#while True:
#	#data_stat_get(ID)
#	dbgs(ID)
#	ID+=1
#	time.sleep(0.5)



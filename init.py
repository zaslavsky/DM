#!/usr/bin/env python
#-*- encoding: cp1251 -*-
import json, urllib, xlrd, xlwt, time, pymongo
from xlutils.copy import copy



client = pymongo.MongoClient("localhost", 27017)
db=client.WOT

BORDER=5000
ID=1681638
MY_ID=1680926

APP_ID="09be322fee8ba81d502df3cd5a03a6c5"

url_info = "http://api.worldoftanks.ru/wot/encyclopedia/tankinfo/?application_id="+APP_ID 
url_user_tanks = "http://api.worldoftanks.ru/wot/tanks/stats/?application_id="+APP_ID
url_stats = "http://api.worldoftanks.ru/wot/account/info/?application_id="+APP_ID
url_tanks_list = "http://api.worldoftanks.ru/wot/encyclopedia/tanks/?application_id="+APP_ID
url_tanks_lib = "http://api.worldoftanks.ru/wot/encyclopedia/tanks/?application_id=" +APP_ID

profile="&account_id="


########################################################################

xls=xlwt.Workbook()
file_players=xls.add_sheet('Players')
file_tanks=xls.add_sheet('Tanks')

lib = list(db.lib.find())
tanklib=lib[0]["data"]

#source_filename = "mask.xls"
#destination_filename = "data.xls"

#read_book = xlrd.open_workbook(source_filename, on_demand=True)  # Открываем исходный документ
#read_sheet = read_book.get_sheet(0)  # Читаем из первого листа
#localdata = copy(read_book)  # Копируем таблицу в память, в неё мы ниже будем записывать
#xls = localdata.get_sheet(0)  # Будем записывать в первый лист

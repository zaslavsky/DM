#!/usr/bin/env python
#-*- encoding: cp1251 -*-
import json, urllib, xlrd, xlwt, time, pymongo
from xlutils.copy import copy



I=1680926

ID=I

APP_ID="09be322fee8ba81d502df3cd5a03a6c5"

url_info = "http://api.worldoftanks.ru/wot/encyclopedia/tankinfo/?application_id="+APP_ID 
url_user_tanks = "http://api.worldoftanks.ru/wot/tanks/stats/?application_id="+APP_ID
url_stats = "http://api.worldoftanks.ru/wot/account/info/?application_id="+APP_ID
profile="&account_id="

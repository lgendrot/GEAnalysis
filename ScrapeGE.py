import requests
from bs4 import BeautifulSoup
import re
import os
import urllib2
import time
import datetime
import GrandExchange
import json



url_names = []
item_names = {}
item_ids = [1944]

def getItemNames(item_numbers):
	#takes a list of Runescape Item IDs as integers or strings
	#for ever item in my ID list
	for item_id in item_numbers:
		item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='+str(item_id)
		item_response = requests.get(item_url)
		item_json = item_response.json()
		item_names[str(item_json['item']['id'])] = item_json['item']['name']


getItemNames(GrandExchange.item_ids)

for item_id in item_names:
	url_names.append(item_id+ "-" +item_names[item_id].replace(" ", "-"))


dates = []
prices = []

pagenums = range(1, 60)

for item_url in url_names:
	item_id = re.split(r'([0-9]*)', item_url)[1]
	for pagenum in pagenums:
		url = "http://www.grandexchangewatch.com/item/" + item_url + "?start=" + str(pagenum)
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		cal = soup.find_all("div", {"id": "calendar-container"})

		tds = cal[0].contents[5].find_all("td")

		date_id_1 = [x*6 for x in range(10)]
		date_id_2 = [x+3 for x in date_id_1]

		price_id_1 = [1+(x*6) for x in range(10)]
		price_id_2 = [x+3 for x in price_id_1]

		for i in date_id_1:
			dates.append(tds[i].text)
		for y in date_id_2:
			dates.append(tds[y].text)

		for i in price_id_1:
			prices.append(tds[i].text.replace(",",'').replace("gp",""))
		for y in price_id_2:
			prices.append(tds[i].text.replace(",",'').replace("gp",""))



	dates.reverse()
	prices.reverse()

	f = open(item_names[item_id]+'.csv', 'a+')
	for date in dates:
		ind = dates.index(date)
		entry = str(time.mktime(time.strptime(date, "%B %d, %Y"))) + "," + prices[ind] + "\n"
		f.write(entry)
	f.close()

	dates[:] = []
	prices[:] = []










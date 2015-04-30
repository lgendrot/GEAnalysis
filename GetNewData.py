import requests
from bs4 import BeautifulSoup
import GrandExchange
from GrandExchange import getItemNames
import re
import csv
import os
import urllib2
import json
import time
import numpy as np
import pprint
import datetime
import csv
from itertools import izip



urls = []
pagenums = range(1, 60)
names = []
url_names = []
getItemNames(GrandExchange.item_ids)

for item_id in GrandExchange.item_names:
	url_names.append(item_id+ "-" +GrandExchange.item_names[item_id].replace(" ", "-"))



dates = []
prices = []

for item_url in url_names:
	item_id = re.split(r'([0-9]*)', item_url)[1]
	url = "http://www.grandexchangewatch.com/item/" + item_url
	r = requests.get(url)

	soup = BeautifulSoup(r.content)

	cal = soup.find_all("div", {"id": "calendar-container"})

	for item in cal:
		tds = item.contents[5].find_all("td")

		date_id_1 = [x*6 for x in range(10)]
		date_id_2 = [x+3 for x in date_id_1]

		price_id_1 = [1+(x*6) for x in range(10)]
		price_id_2 = [x+3 for x in price_id_1]




		dates.append(tds[date_id_1[0]].text)



		srch = re.search(r'(?!0)(\d{1,3}(\,\d{3})+)|(\d+)', tds[price_id_1[0]].text).group(0)
		prices.append(srch.replace(",",''))



	f = open(GrandExchange.item_names[item_id]+'.csv', 'a+')
	for date in dates:
		ind = dates.index(date)
		entry = str(time.mktime(time.strptime(date, "%B %d, %Y"))) + "," + prices[ind] + "\n"
		f.write(entry)
	f.close()

	dates[:] = []
	prices[:] = []
import os
import urllib2
import json
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import pprint
import datetime
import csv
from itertools import izip

item_ids = ['1944', '556', '314', '53', '453', '440', '227', '554', '555', '561', '560', '563', '1777']
reserve_ids = ['12183', '557', '1515', '444', '559', '449', '377', '447', '2359', '434']


item_t = []
daily_price = []
item_dt = []

item_names = {}


def getItemNames(item_numbers):
	#for ever item in my ID list
	for item_id in item_numbers:
		item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='+str(item_id)
		item_response = urllib2.urlopen(item_url)
		item_html = str(item_response.read())
		item_json = json.loads(item_html)
 
		item_names[str(item_json['item']['id'])] = item_json['item']['name']




# def graphRawFX():
def getData(item_numbers):

	getItemNames(item_numbers)

	for item_id in item_numbers:
		url = 'http://services.runescape.com/m=itemdb_rs/api/graph/'+ str(item_id) + '.json'
		response = urllib2.urlopen(url)
		html = response.read()
		html = str(html)
		json_object = json.loads(html)


		prices = json_object["daily"]


		for key in prices:
			item_t.append(int(key))
			daily_price.append(prices[str(key)])

		item_t.sort()

		for t in item_t:
			item_dt.append(datetime.datetime.fromtimestamp(t/1000).strftime('%Y-%m-%d'))

		with open(item_names[item_id]+'.csv', 'wb') as f:
			writer = csv.writer(f)
			writer.writerows(izip(item_t, daily_price))

		item_t[:] = []
		daily_price[:] = []
		item_dt[:] = []
		time.sleep(2)


def getNewData(item_numbers):

	getItemNames(item_numbers)

	for item_id in item_numbers:
		item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='+str(item_id)
		item_response = urllib2.urlopen(item_url)
		item_html = item_response.read()
		item_html = str(item_html)
		item_json = json.loads(item_html)
 
		item_price = item_json['item']['current']['price']
		item_time = int(time.time())

		entry = str(item_time) + ',' + str(item_price) + '\n'

		f = open(item_names[item_id]+'.csv', 'ab')
		f.write(entry)
		f.close()

		time.sleep(2)









# daily_index = range(1, len(prices)+1)


# fit = plt.figure(figsize=(20,10))
# ax1 = plt.subplot2grid((169,169), (0,0), rowspan=169, colspan=169)

# ax1.plot(times, daily_price)

# plt.grid(True)
# plt.show()



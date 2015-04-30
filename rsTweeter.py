import pandas 
import csv
import tweepy
import time


colnames = ['ItemName', 'ItemID', 'ItemPrice', 'PriceChangePercent', 'NewItemPrice']

InterestingItems = pandas.read_csv('ItemsOfInterest.csv', names=colnames)

ItemNames = list(InterestingItems.ItemName)
ItemID = list(InterestingItems.ItemID)
ItemPrice = list(InterestingItems.ItemPrice)
PriceChangePercent = list(InterestingItems.PriceChangePercent)
NewItemPrice = list(InterestingItems.NewItemPrice)



CONSUMER_KEY = 'zzPeqec9QfHNJKTZwvKDdekcP'
CONSUMER_SECRET = 'ne3xA1cliohzsuNFKBP9A0UO6ltqh2cQDAAbPExSyn5A1Y3Fe4'
ACCESS_KEY = '3045170317-IEv5Q5J5ZPhSMipvvfn2TUaZSoUujEqZ6IFZfUq'
ACCESS_SECRET = 'g2OKOFzfN0Pc7L7x59GOLUU2yd5c4udgk9fPh7I0jYL3B'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


for name in ItemNames:
	tweetstring = "The price of " + str(name) + " is projected to rise "+ str(PriceChangePercent[ItemNames.index(name)]) + "%, from a price of (" + str(ItemPrice[ItemNames.index(name)]) + "gp) to a price of " +"(" +str(NewItemPrice[ItemNames.index(name)])+ "gp)"
	api.update_status(status=tweetstring)
	time.sleep(900)


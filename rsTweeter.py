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



CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


for name in ItemNames:
	tweetstring = "The price of " + str(name) + " is projected to rise "+ str(PriceChangePercent[ItemNames.index(name)]) + "%, from a price of (" + str(ItemPrice[ItemNames.index(name)]) + "gp) to a price of " +"(" +str(NewItemPrice[ItemNames.index(name)])+ "gp)"
	api.update_status(status=tweetstring)
	time.sleep(900)


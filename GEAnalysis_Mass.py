import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import urllib2
import json

totalTimeStart = time.time()




def percentChange(startPoint, currentPoint):
	try:
		x = ((currentPoint - float(startPoint)) / abs(startPoint)) * 100
		if x == 0.0:
			return 0.00000000001
		else:
			return x
	except:
		return 0.00000000001

def patternStorage():
	x = len(item_price) - 20
	y = 20

	while y < x:
		pattern = []
		patStartTime = time.time()

		for i in range(19,-1,-1):
			pattern.append(percentChange(item_price[y-20], item_price[y-i]))


		outcomeRange = item_price[y+1:y+21]
		currentPoint = item_price[y]
		patternAr.append(pattern)

		try:
			avgOutcome = reduce(lambda x, y: x+y, outcomeRange / len(outcomeRange))
		except Exception, e:
			print str(e)
			avgOutcome=0

		futureOutcome = percentChange(currentPoint, avgOutcome)


		performanceAr.append(futureOutcome)

		y+=1

	patEndTime = time.time()
	print 'Pattern storage took: ', patEndTime - patStartTime , 'seconds'

def currentPattern():
	cp = []
	for i in range(20,0,-1):
		cp.append(percentChange(item_price[-21], item_price[-i]))
	global patForRec
	patForRec = cp

def patternRecognition():
	
	predictedOutcomesAr = []
	patFound = 0
	plotPatAr = []

	sims = []
	for eachPattern in patternAr:
		for i in range(0, 20):
			sims.append(100.0 - abs(percentChange(eachPattern[i], patForRec[i])))

		howSim = (sim1 + sim2 + sim3 + sim4 + sim5 + sim6 + sim7 + sim8 + sim9 + sim10+
							sim11 + sim12 + sim13 + sim14 + sim15 + sim16 + sim17 + sim18 + sim19 + sim20) / 20.0

		if howSim > 75:
			patFound = 1
			xp = range(1, 21)
			similarPatterns.append(eachPattern)

		
	if patFound == 1:
		for eachpatt in similarPatterns:
			futurePoints = patternAr.index(eachpatt)
			predictedOutcomesAr.append(performanceAr[futurePoints])
			if performanceAr[futurePoints] > patForRec[19]:
					positiveOutcomes += 1
		print positiveOutcomes
	
		predictedAvgOutcome = reduce(lambda x, y: x+y, predictedOutcomesAr) / len(predictedOutcomesAr)

		print predictedAvgOutcome
		print patForRec[19]
		
		if predictedAvgOutcome > patForRec[19]:
			Positive = 1
			OutcomePrediction = predictedAvgOutcome






def getItemNames(item_numbers):
	for item_id in item_numbers:
		item_url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='+str(item_id)
		item_response = urllib2.urlopen(item_url)
		item_html = item_response.read()
		item_html = str(item_html)
		item_json = json.loads(item_html)
 
		item_names[str(item_json['item']['id'])] = item_json['item']['name']

item_ids = ['1944', '556', '314', '53', '453', '440', '227', '554', '561', '560', '563', '1777']




interestingItems = []
item_names = {}
patternAr = []
performanceAr = []
patForRec = []
positiveOutcomes = 0
Positive = 0
OutcomePrediction = 0

getItemNames(item_ids)

def Analyze():
	patternStorage()
	currentPattern()
	patternRecognition()
	
	if positiveOutcomes > 1 and Positive == 1:
		priceChangePercent = int(abs(patForRec[19]-OutcomePrediction))/100.0
		newPrice = ((priceChangePercent)*item_price[-1]) + item_price[-1]
		interestingItems.append(str(item_names[item]) + "," + str(item) + "," + str(item_price[-1]) + "," + str(priceChangePercent) + "," + str(newPrice))
		print "interesting items appended"
	
	patternAr[:] = []
	performanceAr[:] = []
	patForRec[:] = []
	positiveOutcomes[:] = []
	Positive[:] = []


for item in item_names:
	datestamp, gold = np.loadtxt(str(item_names[item])+".csv", unpack=True,
																									delimiter=',')
	item_price = gold
	Analyze()




f = open('ItemsOfInterest.csv', 'w+')
for item in interestingItems:
	f.write(str(item)+'\n')
f.close()




	
	# totalTime = time.time() - totalTimeStart
	# print 'total time to run =', totalTime
	










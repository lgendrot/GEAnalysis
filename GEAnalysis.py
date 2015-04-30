# import GrandExchange as GEData
import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

totalTimeStart = time.time()

datestamp, gold = np.loadtxt('Air rune.csv', unpack=True,
														delimiter=',')
item_price = gold



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

	for eachPattern in patternAr:
		sims = []
		for i in range(0, 20):
			sims.append(100.0 - abs(percentChange(eachPattern[i], patForRec[i])))

		howSim = np.average(sims)
		print howSim


		if howSim > 75:
			patFound = 1

			xp = range(1, 21)
			plotPatAr.append(eachPattern)



	if patFound == 1:
		fig = plt.figure(figsize = (10,6))

		for eachpatt in plotPatAr:
			futurePoints = patternAr.index(eachpatt)
			if performanceAr[futurePoints] > patForRec[19]:
				pcolor = '#24bc00'
			else:
				pcolor = '#d40000'
			plt.plot(xp, eachpatt)
			predictedOutcomesAr.append(performanceAr[futurePoints])
			plt.scatter(27, performanceAr[futurePoints], c=pcolor, alpha=.3)
			

		predictedAvgOutcome = reduce(lambda x, y: x+y, predictedOutcomesAr) / len(predictedOutcomesAr)

		plt.scatter(24, predictedAvgOutcome, c='b', s=25)


		plt.plot(xp, patForRec, '#54fff7', linewidth = 3)
		plt.grid(True)
		plt.title("Fire Rune")
		plt.show()


patternAr = []
performanceAr = []

patternStorage()
currentPattern()
patternRecognition()
	










import numpy as np


### SIMPLE MOVING AVERAGE ###
#############################

dataset = #My price data

def movingAverage(values, window):
	weights = np.repeat(1.0, window)/window
	smAVGs = np.convolve(values, weights,'valid')
	return smAVGs


def expMovingAverage(values, window):
	weights = np.exp(np.linspace(-1., 0., window))
	weights /= weights.sum()

	a = np.convolve(values, weights)[:len(values)]
	a[:window]=a[window]
	return a


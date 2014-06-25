##import matplotlib.pylab as pl
import scipy as sp
import scipy.optimize as op
import numpy.random as rand
import sys, os, time

def scoreGen(noResults, minVal, maxVal):
    return rand.random_integers(minVal, maxVal, noResults)

def weightedScore(weighting, marksRaw):
    if len(weighting)!=len(marksRaw):
        return "Mismatch in lengths"
    else:
        sumMark = 0.0
        for i in range(0,len(weighting)):
            sumMark+=weighting[i]*marksRaw[i]

    return sumMark


testWeight = [0.5,0.3,0.2]
###### Check weighting sums properly 
if sum(testWeight)!=1.0:
    print "Weighting doesn't sum properly"

noOfModules = 3
minMark = 0
maxMark = 100
totalScores=[]

for i in range(0,1000):
    resultsBlock = scoreGen(noOfModules, minMark, maxMark)
    totalScores.append(weightedScore(testWeight, resultsBlock))
print sp.mean(totalScores)

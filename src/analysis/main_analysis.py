# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Main training script. Requires several dependencies.
"""
# This must occur first
from __future__ import division
# Import custom modules
from marchmadness import *
from marchmadness.rdsfunctions import rdshandling
from marchmadness.marchmadnessfunctions import marchmadnessfunctions
# Import all the things
import os
import numpy as np
from random import randint
import os
from os import path
import sklearn
import pandas as pd
import numpy as np
import collections
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn import tree
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Convolution1D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from sklearn.model_selection import cross_val_score
from keras.utils import np_utils
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import sys
from sklearn.ensemble import GradientBoostingRegressor
import math
import csv
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import classification_report
import urllib
from sklearn.svm import LinearSVC
from utils import *
from datetime import datetime

# Prepare the team dataframe
teamsdf = rdshandling.readremoteRDSdata('https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/Teams.rds?raw=true')

# Read compact data in
regularSeasonCompactDf = rdshandling.readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/RegularSeasonCompactResults.rds?raw=true')

# Read advanced data
tourneyResultsDf = rdshandling.readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/TourneyWinners.rds?raw=true')

# Get training file for 1993 to 2019
tourneyCompactDf = rdshandling.readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/NCAATourneyCompactResults.rds?raw=true')

# Get tourney seeds
tourneySeedsDf = rdshandling.readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/NCAATourneySeeds.rds?raw=true')

# Get conference information
confDf = rdshandling.readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/Conference.rds?raw=true')


# Train the model for all years
years = range(1993, 2019)
# Saves the team vectors for the following years
saveYears = range(2015, 2019)
if os.path.exists("Data/PrecomputedMatrices/xTrain.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain.npy"):
    print ('There is already a precomputed xTrain and yTrain model set.')
    response = input('Do you want to remove these files and create a new training set? [y/N] ')
    if (response == 'y'):
        os.remove("Data/PrecomputedMatrices/xTrain.npy")
        os.remove("Data/PrecomputedMatrices/yTrain.npy")
        createAndSave(years, saveYears)
    else: 
        print ('Quitting trainer now')
else:
    marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
  
# Load training set that we just made
if os.path.exists("Data/PrecomputedMatrices/xTrain.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain.npy"):
	xTrain = np.load("Data/PrecomputedMatrices/xTrain.npy")
	yTrain = np.load("Data/PrecomputedMatrices/yTrain.npy")
	print ("Shape of xTrain:", xTrain.shape)
	print ("Shape of yTrain:", yTrain.shape)
else:
	print ('Training models not found!')
	sys.exit()

# Current year needs to be filled
curYear = 2019

model = GradientBoostingRegressor(n_estimators=100, max_depth=5)

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ',
           'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]
numTrials = 1

for i in range(numTrials):
    X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    startTime = datetime.now() # For some timing stuff
    results = model.fit(X_train, Y_train)
    preds = model.predict(X_test)

    preds[preds < .5] = 0
    preds[preds >= .5] = 1
    localAccuracy = np.mean(preds == Y_test)
    accuracy.append(localAccuracy)
    print ("Finished run #" + str(i) + ". Accuracy = " + str(localAccuracy))
    print ("Time taken: " + str(datetime.now() - startTime))
if numTrials != 0:
	print ("Avg accuracy:", sum(accuracy)/len(accuracy))

trainedModel = marchmadnessfunctions.trainModel(xTrain, yTrain)

# Not going to do any hyperparameter optimization pthtbbttbtbh
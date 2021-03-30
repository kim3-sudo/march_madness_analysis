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
from sklearn.model_selection import train_test_split
import sys
from sklearn.ensemble import GradientBoostingRegressor
from datetime import datetime
from tqdm import tqdm

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

"""
# Create a training data set for all years
years = range(1993, 2019)
# Saves the team vectors for the following years
saveYears = range(2015, 2019)
if os.path.exists("Data/PrecomputedMatrices/xTrain.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain.npy"):
    print ('There is already a precomputed xTrain and yTrain model set.')
    response = input('Do you want to remove these files and create a new training set? [y/N] ')
    if (response == 'y'):
        os.remove("Data/PrecomputedMatrices/xTrain.npy")
        os.remove("Data/PrecomputedMatrices/yTrain.npy")
        marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
    else: 
        print ('Quitting trainer now')
else:
    print('No precomputed matrices found')
    print('Creating a new sample subset')
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

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ', 'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]

# Choose epochs here
numTrials = 10

# Starting model training
for i in tqdm(range(numTrials)):
    X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    startTime = datetime.now() # For some timing stuff
    results = model.fit(X_train, Y_train)
    preds = model.predict(X_test)

    preds[preds < .5] = 0
    preds[preds >= .5] = 1
    localAccuracy = np.mean(preds == Y_test)
    accuracy.append(localAccuracy)
    print()
    print ("Finished run #" + str(i) + ". Accuracy = " + str(localAccuracy))
    print ("Time taken: " + str(datetime.now() - startTime))
if numTrials != 0:
	print ("Avg accuracy:", sum(accuracy)/len(accuracy))

trainedModel = marchmadnessfunctions.trainModel(xTrain, yTrain)
"""

##########################################
# Create a training data set for 2017-2019
years = range(2017, 2019)
# Saves the team vectors for the following years
saveYears = range(2017, 2019)
if os.path.exists("Data/PrecomputedMatrices/xTrain2017.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2017.npy"):
    print ('There is already a precomputed xTrain2017 and yTrain2017 model set.')
    response = input('Do you want to remove these files and create a new training set? [y/N] ')
    if (response == 'y'):
        os.remove("Data/PrecomputedMatrices/xTrain2017.npy")
        os.remove("Data/PrecomputedMatrices/yTrain2017.npy")
        marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
    else: 
        print ('Quitting trainer now')
else:
    print('No precomputed matrices found')
    print('Creating a new sample subset')
    marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
  
# Load training set that we just made
if os.path.exists("Data/PrecomputedMatrices/xTrain2017.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2017.npy"):
	xTrain = np.load("Data/PrecomputedMatrices/xTrain2017.npy")
	yTrain = np.load("Data/PrecomputedMatrices/yTrain2017.npy")
	print ("Shape of xTrain:", xTrain.shape)
	print ("Shape of yTrain:", yTrain.shape)
else:
	print ('Training models not found!')
	sys.exit()

# Current year needs to be filled
curYear = 2019

model = GradientBoostingRegressor(n_estimators=100, max_depth=5)

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ', 'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]

# Choose epochs here
numTrials = 10

# Starting model training
for i in tqdm(range(numTrials)):
    X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    startTime = datetime.now() # For some timing stuff
    results = model.fit(X_train, Y_train)
    preds = model.predict(X_test)

    preds[preds < .5] = 0
    preds[preds >= .5] = 1
    localAccuracy = np.mean(preds == Y_test)
    accuracy.append(localAccuracy)
    print()
    print ("Finished run #" + str(i) + ". Accuracy = " + str(localAccuracy))
    print ("Time taken: " + str(datetime.now() - startTime))
if numTrials != 0:
	print ("Avg accuracy:", sum(accuracy)/len(accuracy))

trainedModel = marchmadnessfunctions.trainModel(xTrain, yTrain)

##########################################
# Create a training data set for 2018-2019
years = range(2018, 2019)
# Saves the team vectors for the following years
saveYears = range(2018, 2019)
if os.path.exists("Data/PrecomputedMatrices/xTrain2018.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2018.npy"):
    print ('There is already a precomputed xTrain2018 and yTrain2018 model set.')
    response = input('Do you want to remove these files and create a new training set? [y/N] ')
    if (response == 'y'):
        os.remove("Data/PrecomputedMatrices/xTrain2018.npy")
        os.remove("Data/PrecomputedMatrices/yTrain2018.npy")
        marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
    else: 
        print ('Quitting trainer now')
else:
    print('No precomputed matrices found')
    print('Creating a new sample subset')
    marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
  
# Load training set that we just made
if os.path.exists("Data/PrecomputedMatrices/xTrain2018.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2018.npy"):
	xTrain = np.load("Data/PrecomputedMatrices/xTrain2018.npy")
	yTrain = np.load("Data/PrecomputedMatrices/yTrain2018.npy")
	print ("Shape of xTrain:", xTrain.shape)
	print ("Shape of yTrain:", yTrain.shape)
else:
	print ('Training models not found!')
	sys.exit()

# Current year needs to be filled
curYear = 2019

model = GradientBoostingRegressor(n_estimators=100, max_depth=5)

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ', 'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]

# Choose epochs here
numTrials = 10

# Starting model training
for i in tqdm(range(numTrials)):
    X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    startTime = datetime.now() # For some timing stuff
    results = model.fit(X_train, Y_train)
    preds = model.predict(X_test)

    preds[preds < .5] = 0
    preds[preds >= .5] = 1
    localAccuracy = np.mean(preds == Y_test)
    accuracy.append(localAccuracy)
    print()
    print ("Finished run #" + str(i) + ". Accuracy = " + str(localAccuracy))
    print ("Time taken: " + str(datetime.now() - startTime))
if numTrials != 0:
	print ("Avg accuracy:", sum(accuracy)/len(accuracy))

trainedModel = marchmadnessfunctions.trainModel(xTrain, yTrain)

##########################################
# Create a training data set for 2019 only
years = range(2019, 2019)
# Saves the team vectors for the following years
saveYears = range(2019, 2019)
if os.path.exists("Data/PrecomputedMatrices/xTrain2019.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2019.npy"):
    print ('There is already a precomputed xTrain2019 and yTrain2019 model set.')
    response = input('Do you want to remove these files and create a new training set? [y/N] ')
    if (response == 'y'):
        os.remove("Data/PrecomputedMatrices/xTrain2019.npy")
        os.remove("Data/PrecomputedMatrices/yTrain2019.npy")
        marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
    else: 
        print ('Quitting trainer now')
else:
    print('No precomputed matrices found')
    print('Creating a new sample subset')
    marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)
  
# Load training set that we just made
if os.path.exists("Data/PrecomputedMatrices/xTrain2019.npy") and os.path.exists("Data/PrecomputedMatrices/yTrain2019.npy"):
	xTrain = np.load("Data/PrecomputedMatrices/xTrain2019.npy")
	yTrain = np.load("Data/PrecomputedMatrices/yTrain2019.npy")
	print ("Shape of xTrain:", xTrain.shape)
	print ("Shape of yTrain:", yTrain.shape)
else:
	print ('Training models not found!')
	sys.exit()

# Current year needs to be filled
curYear = 2019

model = GradientBoostingRegressor(n_estimators=100, max_depth=5)

categories=['Wins','PPG','PPGA','PowerConf','3PG', 'APG','TOP','Conference Champ','Tourney Conference Champ', 'Seed','SOS','SRS', 'RPG', 'SPG', 'Tourney Appearances','National Championships','Location']
accuracy=[]

# Choose epochs here
numTrials = 10

# Starting model training
for i in tqdm(range(numTrials)):
    X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    startTime = datetime.now() # For some timing stuff
    results = model.fit(X_train, Y_train)
    preds = model.predict(X_test)

    preds[preds < .5] = 0
    preds[preds >= .5] = 1
    localAccuracy = np.mean(preds == Y_test)
    accuracy.append(localAccuracy)
    print()
    print ("Finished run #" + str(i) + ". Accuracy = " + str(localAccuracy))
    print ("Time taken: " + str(datetime.now() - startTime))
if numTrials != 0:
	print ("Avg accuracy:", sum(accuracy)/len(accuracy))

trainedModel = marchmadnessfunctions.trainModel(xTrain, yTrain)


# Not going to do any hyperparameter optimization pthtbbttbtbh
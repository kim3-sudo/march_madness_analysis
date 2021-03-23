# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Main training script. Requires several dependencies.
"""

from marchmadness import *
from marchmadness.rdsfunctions import rdshandling
from marchmadness.marchmadnessfunctions import marchmadnessfunctions

# Import all the things
import os

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
        print ('Quitting now')
else:
    marchmadnessfunctions.createAndSave(years, saveYears, regularSeasonCompactDf, tourneyCompactDf, teamsdf, tourneySeedsDf, confDf, tourneyResultsDf)

# Not going to do any hyperparameter optimization pthtbbttbtbh
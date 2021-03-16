# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Script-specific function definitions
"""

from rdsfunctions import *
# Import all the things
import pyreadr
from random import randint
import os
from os import path
import sklearn
from __future__ import division
import pandas as pd
import numpy as np
import collections
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn import tree
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, Convolution1D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD
from sklearn.cross_validation import cross_val_score
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

class marchmadnessfunctions:
    def checkpower6conference(TeamID = 0):
        """
        Checks if a team is one of the Power 6 conferences
    
        Parameters
        ----------
        TeamID : int
            An integer team ID. The default is 0.
    
        Returns
        -------
        bool
            Returns True if the team is a Power 6 school or False otherwise.
    
        """
        teamName = teamsdf.values[TeamID-1101][1]
        if (teamName in ACCTEAMS or teamName in BIG10TEAMS or teamName in BIG12TEAMS or teamName in SECTEAMS or teamName in PAC12TEAMS or teamName in BIGEASTTEAMS):
            return True
        else:
            return False
    
    def getteamID(name):
        """
        Returns the team ID
    
        Parameters
        ----------
        name : string
            The standardized team name as stored in dataset.
    
        Returns
        -------
        int
            The team ID.
    
        """
        return teamsdf[teamsdf['TeamName'] == name].values[0][0]
    
    def getteamname(TeamID):
        """
        Returns the name of the team
    
        Parameters
        ----------
        TeamID : int
            The team ID.
    
        Returns
        -------
        string
            The standardized team name as stored in dataset.
    
        """
        return teamsdf[teamsdf['TeamID'] == TeamID].values[0][1]
    
    def getnumchampionships(TeamID):
        name = getteamname(TeamID)
        return NCAAChampionsList.count(name)
    
    def getlistforURL(team_list):
        """
        Usage:
            getlistforURL(teamList)
    
        Parameters
        ----------
        team_list : list of strings
            The list of teams to get the URLs for.
    
        Returns
        -------
        None.
    
        """
        team_list = [x.lower() for x in team_list]
        team_list = [t.replace(' ', '-') for t in team_list]
        team_list = [t.replace('st', 'state') for t in team_list]
        team_list = [t.replace('northern-dakota', 'north-dakota') for t in team_list]
        team_list = [t.replace('nc-', 'north-carolina-') for t in team_list]
        team_list = [t.replace('fl-', 'florida-') for t in team_list]
        team_list = [t.replace('ga-', 'georgia-') for t in team_list]
        team_list = [t.replace('lsu', 'louisiana-state') for t in team_list]
        team_list = [t.replace('maristate', 'marist') for t in team_list]
        team_list = [t.replace('stateate', 'state') for t in team_list]
        team_list = [t.replace('northernorthern', 'northern') for t in team_list]
        team_list = [t.replace('usc', 'southern-california') for t in team_list]
        base = 'http://www.sports-reference.com/cbb/schools/'
        for team in team_list:
            url = base + team + '/'
    
    def handlecases(arr):
        """
        Handles the fringe cases for Florida and FL, as well as State and St
    
        Parameters
        ----------
        arr : TYPE
            DESCRIPTION.
    
        Returns
        -------
        arr : TYPE
            DESCRIPTION.
    
        """
        indices = []
        listLen = len(arr)
        for i in range(listLen):
            if (arr[i] == 'St' or arr[i] == 'FL'):
                indices.append(i)
        for p in indices:
            arr[p-1] = arr[p-1] + ' ' + arr[p]
        for i in range(len(indices)): 
            arr.remove(arr[indices[i] - i])
        return arr
    
    
    def checkconferencechamp(TeamID, year):
        """
        Checks if a school is the conference champion
    
        Parameters
        ----------
        TeamID : int
            The team ID.
        year : int
            The year to look up data for as a four-digit number.
    
        Returns
        -------
        bool
            Returns True if the school is the conference champion or False otherwise.
    
        """
        year_conf_pd = conference_pd[conference_pd['Year'] == year]
        champs = year_conf_pd['Regular Season Champ'].tolist()
        # For handling cases where there is more than one champion
        champs_separated = [words for segments in champs for words in segments.split()]
        name = getTeamName(TeamID)
        champs_separated = handleCases(champs_separated)
        if (name in champs_separated):
            return True
        else:
            return False
    
    def checkconferencetourneychamp(TeamID, year):
        """
        Check if a school is the conference tournament champion
    
        Parameters
        ----------
        TeamID : int
            The team ID.
        year : int
            The year to look up data for as a four-digit number.
    
        Returns
        -------
        bool
            Returns True if the school is the conference champion or False otherwise.
    
        """
        year_conf_pd = conference_pd[conference_pd['Year'] == year]
        champs = year_conf_pd['Tournament Champ'].tolist()
        name = getTeamName(TeamID)
        if (name in champs):
            return True
        else:
            return False
    
    def gettourneyappearances(TeamID):
        """
        Get the number of times a school has appeared in the tournament
    
        Parameters
        ----------
        TeamID : int
            The team ID.
    
        Returns
        -------
        int
            The number of appearances in March Madness.
    
        """
        return len(tourney_seeds_pd[tourney_seeds_pd['Team'] == TeamID].index)
    
    def handleDifferentCSV(df):
        """
        The stats CSV is a lit different in terms of naming. Just some data cleaning
    
        Parameters
        ----------
        df : pandas dataframe
            The dataframe to clean.
    
        Returns
        -------
        df : pandas dataframe
            The preprocessed dataframe with replaced values.
    
        """
        # 
        df['School'] = df['School'].replace('(State)', 'St', regex=True) 
        df['School'] = df['School'].replace('Albany (NY)', 'Albany NY') 
        df['School'] = df['School'].replace('Boston University', 'Boston Univ')
        df['School'] = df['School'].replace('Central Michigan', 'C Michigan')
        df['School'] = df['School'].replace('(Eastern)', 'E', regex=True)
        df['School'] = df['School'].replace('Louisiana St', 'LSU')
        df['School'] = df['School'].replace('North Carolina St', 'NC State')
        df['School'] = df['School'].replace('Southern California', 'USC')
        df['School'] = df['School'].replace('University of California', 'California', regex=True) 
        df['School'] = df['School'].replace('American', 'American Univ')
        df['School'] = df['School'].replace('Arkansas-Little Rock', 'Ark Little Rock')
        df['School'] = df['School'].replace('Arkansas-Pine Bluff', 'Ark Pine Bluff')
        df['School'] = df['School'].replace('Bowling Green St', 'Bowling Green')
        df['School'] = df['School'].replace('Brigham Young', 'BYU')
        df['School'] = df['School'].replace('Cal Poly', 'Cal Poly SLO')
        df['School'] = df['School'].replace('Centenary (LA)', 'Centenary')
        df['School'] = df['School'].replace('Central Connecticut St', 'Central Conn')
        df['School'] = df['School'].replace('Charleston Southern', 'Charleston So')
        df['School'] = df['School'].replace('Coastal Carolina', 'Coastal Car')
        df['School'] = df['School'].replace('College of Charleston', 'Col Charleston')
        df['School'] = df['School'].replace('Cal St Fullerton', 'CS Fullerton')
        df['School'] = df['School'].replace('Cal St Sacramento', 'CS Sacramento')
        df['School'] = df['School'].replace('Cal St Bakersfield', 'CS Bakersfield')
        df['School'] = df['School'].replace('Cal St Northridge', 'CS Northridge')
        df['School'] = df['School'].replace('East Tennessee St', 'ETSU')
        df['School'] = df['School'].replace('Detroit Mercy', 'Detroit')
        df['School'] = df['School'].replace('Fairleigh Dickinson', 'F Dickinson')
        df['School'] = df['School'].replace('Florida Atlantic', 'FL Atlantic')
        df['School'] = df['School'].replace('Florida Gulf Coast', 'FL Gulf Coast')
        df['School'] = df['School'].replace('Florida International', 'Florida Intl')
        df['School'] = df['School'].replace('George Washington', 'G Washington')
        df['School'] = df['School'].replace('Georgia Southern', 'Ga Southern')
        df['School'] = df['School'].replace('Gardner-Webb', 'Gardner Webb')
        df['School'] = df['School'].replace('Illinois-Chicago', 'IL Chicago')
        df['School'] = df['School'].replace('Kent St', 'Kent')
        df['School'] = df['School'].replace('Long Island University', 'Long Island')
        df['School'] = df['School'].replace('Loyola Marymount', 'Loy Marymount')
        df['School'] = df['School'].replace('Loyola (MD)', 'Loyola MD')
        df['School'] = df['School'].replace('Loyola (IL)', 'Loyola-Chicago')
        df['School'] = df['School'].replace('Massachusetts', 'MA Lowell')
        df['School'] = df['School'].replace('Maryland-Eastern Shore', 'MD E Shore')
        df['School'] = df['School'].replace('Miami (FL)', 'Miami FL')
        df['School'] = df['School'].replace('Miami (OH)', 'Miami OH')
        df['School'] = df['School'].replace('Missouri-Kansas City', 'Missouri KC')
        df['School'] = df['School'].replace('Monmouth', 'Monmouth NJ')
        df['School'] = df['School'].replace('Mississippi Valley St', 'MS Valley St')
        df['School'] = df['School'].replace('Montana St', 'MTSU')
        df['School'] = df['School'].replace('Northern Colorado', 'N Colorado')
        df['School'] = df['School'].replace('North Dakota St', 'N Dakota St')
        df['School'] = df['School'].replace('Northern Illinois', 'N Illinois')
        df['School'] = df['School'].replace('Northern Kentucky', 'N Kentucky')
        df['School'] = df['School'].replace('North Carolina A&T', 'NC A&T')
        df['School'] = df['School'].replace('North Carolina Central', 'NC Central')
        df['School'] = df['School'].replace('Pennsylvania', 'Penn')
        df['School'] = df['School'].replace('South Carolina St', 'S Carolina St')
        df['School'] = df['School'].replace('Southern Illinois', 'S Illinois')
        df['School'] = df['School'].replace('UC-Santa Barbara', 'Santa Barbara')
        df['School'] = df['School'].replace('Southeastern Louisiana', 'SE Louisiana')
        df['School'] = df['School'].replace('Southeast Missouri St', 'SE Missouri St')
        df['School'] = df['School'].replace('Stephen F. Austin', 'SF Austin')
        df['School'] = df['School'].replace('Southern Methodist', 'SMU')
        df['School'] = df['School'].replace('Southern Mississippi', 'Southern Miss')
        df['School'] = df['School'].replace('Southern', 'Southern Univ')
        df['School'] = df['School'].replace('St. Bonaventure', 'St Bonaventure')
        df['School'] = df['School'].replace('St. Francis (NY)', 'St Francis NY')
        df['School'] = df['School'].replace('Saint Francis (PA)', 'St Francis PA')
        df['School'] = df['School'].replace('St. John\'s (NY)', 'St John\'s')
        df['School'] = df['School'].replace('Saint Joseph\'s', 'St Joseph\'s PA')
        df['School'] = df['School'].replace('Saint Louis', 'St Louis')
        df['School'] = df['School'].replace('Saint Mary\'s (CA)', 'St Mary\'s CA')
        df['School'] = df['School'].replace('Mount Saint Mary\'s', 'Mt St Mary\'s')
        df['School'] = df['School'].replace('Saint Peter\'s', 'St Peter\'s')
        df['School'] = df['School'].replace('Texas A&M-Corpus Christian', 'TAM C. Christian')
        df['School'] = df['School'].replace('Texas Christian', 'TCU')
        df['School'] = df['School'].replace('Tennessee-Martin', 'TN Martin')
        df['School'] = df['School'].replace('Texas-Rio Grande Valley', 'UTRGV')
        df['School'] = df['School'].replace('Texas Southern', 'TX Southern')
        df['School'] = df['School'].replace('Alabama-Birmingham', 'UAB')
        df['School'] = df['School'].replace('UC-Davis', 'UC Davis')
        df['School'] = df['School'].replace('UC-Irvine', 'UC Irvine')
        df['School'] = df['School'].replace('UC-Riverside', 'UC Riverside')
        df['School'] = df['School'].replace('Central Florida', 'UCF')
        df['School'] = df['School'].replace('Louisiana-Lafayette', 'ULL')
        df['School'] = df['School'].replace('Louisiana-Monroe', 'ULM')
        df['School'] = df['School'].replace('Maryland-Baltimore County', 'UMBC')
        df['School'] = df['School'].replace('North Carolina-Asheville', 'UNC Asheville')
        df['School'] = df['School'].replace('North Carolina-Greensboro', 'UNC Greensboro')
        df['School'] = df['School'].replace('North Carolina-Wilmington', 'UNC Wilmington')
        df['School'] = df['School'].replace('Nevada-Las Vegas', 'UNLV')
        df['School'] = df['School'].replace('Texas-Arlington', 'UT Arlington')
        df['School'] = df['School'].replace('Texas-San Antonio', 'UT San Antonio')
        df['School'] = df['School'].replace('Texas-El Paso', 'UTEP')
        df['School'] = df['School'].replace('Virginia Commonwealth', 'VA Commonwealth')
        df['School'] = df['School'].replace('Western Carolina', 'W Carolina')
        df['School'] = df['School'].replace('Western Illinois', 'W Illinois')
        df['School'] = df['School'].replace('Western Kentucky', 'WKU')
        df['School'] = df['School'].replace('Western Michigan', 'W Michigan')
        df['School'] = df['School'].replace('Abilene Christian', 'Abilene Chr')
        df['School'] = df['School'].replace('Montana State', 'Montana St')
        df['School'] = df['School'].replace('Central Arkansas', 'Cent Arkansas')
        df['School'] = df['School'].replace('Houston Baptist', 'Houston Bap')
        df['School'] = df['School'].replace('South Dakota St', 'S Dakota St')
        df['School'] = df['School'].replace('Maryland-Eastern Shore', 'MD E Shore')
        return df
    
    
    def getseasondata(TeamID, year):
        """
        Get all of the data for a season for a particular team by year and load into memory for ready use
    
        Parameters
        ----------
        TeamID : int
            The team ID.
        year : int
            The year to look up data for as a four-digit number..
    
        Returns
        -------
        list
            DESCRIPTION.
    
        """
        # The data frame below holds stats for every single game in the given year
        year_data_pd = reg_season_compact_pd[reg_season_compact_pd['Season'] == year]
        # Finding number of points per game
        gamesWon = year_data_pd[year_data_pd.WTeamID == TeamID] 
        totalPointsScored = gamesWon['WScore'].sum()
        gamesLost = year_data_pd[year_data_pd.LTeamID == TeamID] 
        totalGames = gamesWon.append(gamesLost)
        numGames = len(totalGames.index)
        totalPointsScored += gamesLost['LScore'].sum()
        
        # Finding number of points per game allowed
        totalPointsAllowed = gamesLost['WScore'].sum()
        totalPointsAllowed += gamesWon['LScore'].sum()
        
        
        stats_SOS_pd = readremoteRDSdata('Data/MMStats/MMStats_'+str(year)+'.csv')
        stats_SOS_pd = handleDifferentCSV(stats_SOS_pd)
        ratings_pd = pd.read_csv('Data/RatingStats/RatingStats_'+str(year)+'.csv')
        ratings_pd = handleDifferentCSV(ratings_pd)
        
        name = getTeamName(TeamID)
        team = stats_SOS_pd[stats_SOS_pd['School'] == name]
        team_rating = ratings_pd[ratings_pd['School'] == name]
        if (len(team.index) == 0 or len(team_rating.index) == 0): #Can't find the team
            total3sMade = 0
            totalTurnovers = 0
            totalAssists = 0
            sos = 0
            totalRebounds = 0
            srs = 0
            totalSteals = 0
        else:
            total3sMade = team['X3P'].values[0]
            totalTurnovers = team['TOV'].values[0]
            if (math.isnan(totalTurnovers)):
                totalTurnovers = 0
            totalAssists = team['AST'].values[0]
            if (math.isnan(totalAssists)):
                totalAssists = 0
            sos = team['SOS'].values[0]
            srs = team['SRS'].values[0]
            totalRebounds = team['TRB'].values[0]
            if (math.isnan(totalRebounds)):
                totalRebounds = 0
            totalSteals = team['STL'].values[0]
            if (math.isnan(totalSteals)):
                totalSteals = 0
        
        #Finding tournament seed for that year
        tourneyYear = tourney_seeds_pd[tourney_seeds_pd['Season'] == year]
        seed = tourneyYear[tourneyYear['Team'] == TeamID]
        if (len(seed.index) != 0):
            seed = seed.values[0][1]
            tournamentSeed = int(seed[1:3])
        else:
            tournamentSeed = 25 #Not sure how to represent if a team didn't make the tourney
        
        # Finding number of wins and losses
        numWins = len(gamesWon.index)
        # There are some teams who may have dropped to Division 2, so they won't have games 
        # a certain year. In this case, we don't want to divide by 0, so we'll just set the
        # averages to 0 instead
        if numGames == 0:
            avgPointsScored = 0
            avgPointsAllowed = 0
            avg3sMade = 0
            avgTurnovers = 0
            avgAssists = 0
            avgRebounds = 0
            avgSteals = 0
        else:
            avgPointsScored = totalPointsScored/numGames
            avgPointsAllowed = totalPointsAllowed/numGames
            avg3sMade = total3sMade/numGames
            avgTurnovers = totalTurnovers/numGames
            avgAssists = totalAssists/numGames
            avgRebounds = totalRebounds/numGames
            avgSteals = totalSteals/numGames
        #return [numWins, sos, srs]
        #return [numWins, avgPointsScored, avgPointsAllowed, checkPower6Conference(TeamID), avg3sMade, avg3sAllowed, avgTurnovers,
        #        tournamentSeed, getStrengthOfSchedule(TeamID, year), getTourneyAppearances(TeamID)]
        return [numWins, avgPointsScored, avgPointsAllowed, checkPower6Conference(TeamID), avg3sMade, avgAssists, avgTurnovers,
               checkConferenceChamp(TeamID, year), checkConferenceTourneyChamp(TeamID, year), tournamentSeed,
                sos, srs, avgRebounds, avgSteals, getTourneyAppearances(TeamID), getNumChampionships(TeamID)]
    
    def compareteams(id_1, id_2, year):
        """
        Compare the results for two teams 
    
        Parameters
        ----------
        id_1 : TYPE
            DESCRIPTION.
        id_2 : TYPE
            DESCRIPTION.
        year : TYPE
            DESCRIPTION.
    
        Returns
        -------
        diff : TYPE
            DESCRIPTION.
    
        """
        team_1 = getSeasonData(id_1, year)
        team_2 = getSeasonData(id_2, year)
        diff = [a - b for a, b in zip(team_1, team_2)]
        return diff
    
    def createseasondict(year):
        """
        Get the team vectors for each NCAA team for a given season

        Parameters
        ----------
        year : int
            The year to look up data for as a four-digit number.

        Returns
        -------
        seasonDictionary : dictionary
            The team vector for each NCAA team for the season

        """
        seasonDictionary = collections.defaultdict(list)
        for team in teamList:
            team_id = teams_pd[teams_pd['Team_Name'] == team].values[0][0]
            team_vector = getSeasonData(team_id, year)
            seasonDictionary[team_id] = team_vector
        return seasonDictionary
    
    def gethomestat(row):
        if (row == 'H'):
            home = 1
        if (row == 'A'):
            home = -1
        if (row == 'N'):
            home = 0
        return home
    
    def createtrainingset(years):
        """
        Split up the number of years in the training set randomly

        Parameters
        ----------
        years : list of ints
            A list of integers to create the training set from. The method subsets the list and creates a training set at random.

        Returns
        -------
        xTrain : numpy object
            A training set for indicator variables.
        yTrain : numpy object
            A training set for response variables.

        """
        totalNumGames = 0
        for year in years:
            season = reg_season_compact_pd[reg_season_compact_pd['Season'] == year]
            totalNumGames += len(season.index)
            tourney = tourney_compact_pd[tourney_compact_pd['Season'] == year]
            totalNumGames += len(tourney.index)
        numFeatures = len(getSeasonData(1181,2012)) #Just choosing a random team and seeing the dimensionality of the vector
        xTrain = np.zeros(( totalNumGames, numFeatures + 1))
        yTrain = np.zeros(( totalNumGames ))
        indexCounter = 0
        for year in years:
            team_vectors = createSeasonDict(year)
            season = reg_season_compact_pd[reg_season_compact_pd['Season'] == year]
            numGamesInSeason = len(season.index)
            tourney = tourney_compact_pd[tourney_compact_pd['Season'] == year]
            numGamesInSeason += len(tourney.index)
            xTrainSeason = np.zeros(( numGamesInSeason, numFeatures + 1))
            yTrainSeason = np.zeros(( numGamesInSeason ))
            counter = 0
            for index, row in season.iterrows():
                w_team = row['WTeamID']
                w_vector = team_vectors[w_team]
                l_team = row['LTeamID']
                l_vector = team_vectors[l_team]
                diff = [a - b for a, b in zip(w_vector, l_vector)]
                home = getHomeStat(row['Wloc'])
                if (counter % 2 == 0):
                    diff.append(home) 
                    xTrainSeason[counter] = diff
                    yTrainSeason[counter] = 1
                else:
                    diff.append(-home)
                    xTrainSeason[counter] = [ -p for p in diff]
                    yTrainSeason[counter] = 0
                counter += 1
            for index, row in tourney.iterrows():
                w_team = row['WTeamID']
                w_vector = team_vectors[w_team]
                l_team = row['LTeamID']
                l_vector = team_vectors[l_team]
                diff = [a - b for a, b in zip(w_vector, l_vector)]
                home = 0 #All tournament games are neutral
                if (counter % 2 == 0):
                    diff.append(home) 
                    xTrainSeason[counter] = diff
                    yTrainSeason[counter] = 1
                else:
                    diff.append(-home)
                    xTrainSeason[counter] = [ -p for p in diff]
                    yTrainSeason[counter] = 0
                counter += 1
            xTrain[indexCounter:numGamesInSeason+indexCounter] = xTrainSeason
            yTrain[indexCounter:numGamesInSeason+indexCounter] = yTrainSeason
            indexCounter += numGamesInSeason
        return xTrain, yTrain
    
    
    def normalizeinput(arr):
        """
        A method that normalizes some variables so that they are comparable (e.g., score to score differential)

        Parameters
        ----------
        arr : array of ints or array of floats
            An array that needs to be normalised.

        Returns
        -------
        arr : array of ints or array of floats
            The normalised array, in the same form that was originally passed in.

        """
        for i in range(arr.shape[1]):
            minVal = min(arr[:,i])
            maxVal = max(arr[:,i])
            arr[:,i] =  (arr[:,i] - minVal) / (maxVal - minVal)
        return arr
    
    def normalize(X):
        """
        An more general array (than normalizeinput()) that normalizes according to mean over standard deviation on a X

        Parameters
        ----------
        X : single float or int
            The frame that is to be normalized, passed in as a single variable.

        Returns
        -------
        single float or int
            The same type as was passed in will be returned in an identical frametype, the normalised variable.

        """
        return (X - np.mean(X, axis = 0)) / np.std(X, axis = 0)
    
    
    def predictGame(team_1_vector, team_2_vector, home):
        """
        Use the neural net to predict game output

        Parameters
        ----------
        team_1_vector : array of ints
            An array of scores that will be used to create a prediction model for team 1.
        team_2_vector : array of ints
            An array of scores that will be used to create a prediction model for team 2.
        home : str
            A single string used to indicate the home (if neutral, what ordinary stadium).

        Returns
        -------
        numpy prediction model
            The predicted game result.

        """
        diff = [a - b for a, b in zip(team_1_vector, team_2_vector)]
        diff.append(home)
        return model.predict([diff]) 
    
    def createPrediction():
        """
        

        Returns
        -------
        None.

        """
        results = [[0 for x in range(2)] for x in range(len(sample_sub_pd.index))]
        for index, row in sample_sub_pd.iterrows():
            matchup_id = row['id']
            year = matchup_id[0:4]
            team1_id = matchup_id[5:9]
            team2_id = matchup_id[10:14]
            team1_vector = getSeasonData(int(team1_id), int(year))
            team2_vector = getSeasonData(int(team2_id), int(year))
            pred = predictGame(team1_vector, team2_vector, 0)
            results[index][0] = matchup_id
            results[index][1] = pred[0]
            #results[index][1] = pred[0][1]
        results = pd.np.array(results)
        firstRow = [[0 for x in range(2)] for x in range(1)]
        firstRow[0][0] = 'id'
        firstRow[0][1] = 'pred'
        with open("result.csv", "wb") as f:
            writer = csv.writer(f)
            writer.writerows(firstRow)
            writer.writerows(results)
    
    def findBestK():
        """
        

        Returns
        -------
        None.

        """
        K = (list)(i for i in range(1,200) if i%2!=0)
        p = []
        for k in K:
            kmeans = KNeighborsClassifier(n_neighbors=k)
            kmeans.fit(X_train, Y_train)
            results = kmeans.fit(X_train, Y_train)
            preds = kmeans.predict(X_test)
            p.append(np.mean(preds == Y_test))
        plt.plot(K, p)
        plt.xlabel('k')
        plt.ylabel('Accuracy')
        plt.title('Selecting k with the Elbow Method')
        plt.show()
    
    def neuralNetwork(loops = 1000):
        """
        Train the neural network 

        Parameters
        ----------
        loops : int, OPTIONAL
            The number of iterations to train by. Corresponds to the number of epochs that will be used. More is better (but takes longer). Default is 1000.

        Returns
        -------
        None.

        """
        accuracy=[]
        dim = 17
        for i in range(loops):
            X_train, X_test, Y_train, Y_test = train_test_split(xTrain, yTrain)
    
            model = Sequential()
            #model.add(Convolution1D(28, 3, border_mode='same', init='normal', input_shape=(dim, 1))) #28 1D filters of length 3
            model.add(Dense(128, init='normal', input_dim = dim))
            model.add(Activation('relu'))
            model.add(Dropout(0.2))
            model.add(Dense(64, init='normal'))
            model.add(Activation('relu'))
            model.add(Dropout(0.1))
            model.add(Dense(16, init='normal'))
            model.add(Activation('relu'))
            model.add(Dense(2, init='normal'))
            model.add(Activation('softmax'))
    
    
            #X_train = X_train.reshape((len(X_train), dim, 1))
            #X_test = X_test.reshape((len(X_test), dim, 1))
            Y_train_categorical = np_utils.to_categorical(Y_train)
            # TRAINING
            model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
            model.fit(X_train, Y_train_categorical, batch_size=64, nb_epoch=10,shuffle=True)
            preds = model.predict(X_test)
            results=[]
            for i in range(preds.shape[0]):
                if preds[i][1] < .5:
                    results.append(0)
                else:
                    results.append(1)
            accuracy.append(np.mean(results == Y_test))
        #accuracy.append(np.mean(predictions == Y_test))
        print ("Accuracy: ", sum(accuracy)/len(accuracy))
    
    def getAllTeamVectors():
        """
        Usage:
            getAllTeamVectors()

        Returns
        -------
        None.

        """
        year = 2016
        numFeatures = len(getSeasonData(1181,2012))
        teamvecs = np.zeros(( 251, numFeatures ))
        teams=[]
        counter = 0
        for team in teamList:
            team_id = teams_pd[teams_pd['Team_Name'] == team].values[0][0]
            team_vector = getSeasonData(team_id, year)
            if (team_vector[0] == 0 or team_vector[4] == 0):
                continue
            teamvecs[counter] = team_vector
            teams.append(team)
            counter += 1
        team = pd.np.array(teams)
        team = np.reshape(team, (team.shape[0], 1))
        with open("allNames.tsv", "wb") as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(team)
        with open("allVecs.tsv", "wb") as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(teamvecs)

    
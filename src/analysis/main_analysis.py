# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Main training script. Requires several dependencies.
"""

import marchmadness

# Prepare the team dataframe
teamsdf = readremoteRDSdata('https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/Teams.rds?raw=true')

# Read compact data in
reg_season_compact_pd = readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/RegularSeasonCompactResults.rds?raw=true')

# Look at the data
reg_season_compact_pd.head()

# All games are on neutral sites, so HFA doesn't really matter...or it shouldn't
# An examination for a different project

# Read advanced data
reg_season_detailed_pd = readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/NCAATourneyDetailedResults.rds?raw=true')

# Look at the advanced data
reg_season_detailed_pd.head()
reg_season_detailed_pd.columns

# Get training file for 1985 to 2018
tourney_compact_pd = readremoteRDSdata(url = 'https://github.com/kim3-sudo/march_madness_data/blob/main/DataFiles/NCAATourneyCompactResults.rds?raw=true')

# Set constant lists for the 68 teams
# Yay vectors
ACCTEAMS = ['Florida St', 'Virginia', 'Clemson', 'Virginia Tech', 'North Carolina', 'Georgia Tech', 'Syracuse', 'Louisville']
PAC12TEAMS = ['Colorado', 'USC', 'Oregon', 'UCLA', 'Oregon St']
SECTEAMS = ['Alabama', 'Arkansas', 'Tennessee', 'Missouri', 'LSU', 'Florida']
BIG10TEAMS = ['Illinois', 'Michigan', 'Ohio St', 'Iowa', 'Purdue', 'Wisconsin', 'Rutgers', 'Maryland', 'Michigan St.']
BIG12TEAMS = ['Baylor', 'Texas', 'Oklahoma St', 'West Virginia', 'Kansas', 'Texas Tech', 'Oklahoma']
BIGEASTTEAMS = ['Villanova', 'Creighton', 'UCONN', 'Georgetown']
WESTCOASTTEAMS = ['Gonzaga', 'BYU']
AACTEAMS = ['Houston', 'Wichita St']
MOUNTAINWESTTEAMS = ['San Diego St']
MISSOURIVALLEYTEAMS = ['Loyola Chicago', 'Drake']
ATLANTIC10TEAMS = ['St Bonaventure', 'VCU']
CUSATEAMS = ['North Texas']
BIGSOUTHTEAMS = ['Winthrop']
BIGWESTTEAMS = ['UC Irvine']
MACTEAMS = ['Ohio']
ATLSUNTEAMS = ['Liberty']
SOUTHERNTEAMS = ['UNC Greensboro']
OHVALLEYTEAMS = ['Morehead St']
PATRIOTTEAMS = ['Colgate']
SOUTHLANDTEAMS = ['Abilene']
BIGSKYTEAMS = ['Eastern Washington']
WACTEAMS = ['Grand Canyon']
MAACTEAMS = ['Iona']
HORIZONTEAMS = ['Cleveland St']
SUMMITTEAMS = ['Oral Roberts']
CAATEAMS = ['Drexel']
AMEASTTEAMS = ['Hartford']
NECTEAMS = ['Mount St Mary\'s']
SUNBELTTEAMS = ['Appalachian St']
SWACTEAMS = ['Texas Southern']
MEACTEAMS = ['Norfolk St']

# Unit test using Georgia Tech
gaTechID = teamsdf[teamsdf['TeamName'] == 'Georgia Tech'].values[0][0]
getseasondata(gaTechID, 2018)

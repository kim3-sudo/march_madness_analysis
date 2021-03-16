# -*- coding: utf-8 -*-
"""
March Madness Analysis
Steven Lucas & Sejin Kim
STAT 306 S21 @ Kenyon College

Script-specific function definitions
"""

from rdsfunctions import *

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
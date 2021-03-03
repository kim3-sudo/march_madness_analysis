### March Madness Analysis
### Steven Lucas & Sejin Kim
### STAT 306 S21 @ Kenyon College

# Prerequisites ----
### You should have already downloaded the tarball with CSV data
### Unroll the tarball and put it in a directory that R has +R permissions for
### Make sure you have a directory that R has +RW permissions to write RDS files to

# Set directories ----
### workingDir is where your CSV files are
### saveDir is where you want to write RDS files out to
workingDir = "c:/Users/kim3/Downloads/march_madness_19"
saveDir = "c:/Users/kim3/Downloads/march_madness_19_rds"

# Process files ----
## Root directory ----
### Read ----
setwd(workingDir)
Prelim2019_Cities <- read.csv("Prelim2019_Cities.csv")
Prelim2019_ConferenceTourneyGames <- read.csv("Prelim2019_ConferenceTourneyGames.csv")
Prelim2019_GameCities <- read.csv("Prelim2019_GameCities.csv")
Prelim2019_RegularSeasonDetailedResults <- read.csv("Prelim2019_RegularSeasonDetailedResults.csv")
Prelim2019_TeamCoaches <- read.csv("Prelim2019_TeamCoaches.csv")

### Write ----
if (file.exists(saveDir)) {
  setwd(saveDir)
} else {
  dir.create(saveDir)
  setwd(saveDir)
}
saveRDS(Prelim2019_Cities, file = "Prelim2019_Cities.rds")
saveRDS(Prelim2019_ConferenceTourneyGames, file = "Prelim2019_ConferenceTourneyGames.rds")
saveRDS(Prelim2019_GameCities, file = "Prelim2019_GameCities.rds")
saveRDS(Prelim2019_RegularSeasonDetailedResults, file = "Prelim2019_RegularSeasonDetailedResults.rds")
saveRDS(Prelim2019_TeamCoaches, file = "Prelim2019_TeamCoaches.rds")

## DataFiles directory ----
### Read ----
setwd(paste(workingDir, "/DataFiles", sep = ""))
DataFiles_Cities <- read.csv("Cities.csv")
DataFiles_Conferences <- read.csv("Conferences.csv")
DataFiles_ConferenceTourneyGames <- read.csv("ConferenceTourneyGames.csv")
DataFiles_GameCities <- read.csv("GameCities.csv")
DataFiles_NCAATourneyCompactResults <- read.csv("NCAATourneyCompactResults.csv")
DataFiles_NCAATourneyDetailedResults <- read.csv("NCAATourneyDetailedResults.csv")
DataFiles_NCAATourneySeedRoundSlots <- read.csv("NCAATourneySeedRoundSlots.csv")
DataFiles_NCAATourneySeeds <- read.csv("NCAATourneySeeds.csv")
DataFiles_NCAATourneySlots <- read.csv("NCAATourneySlots.csv")
DataFiles_RegularSeasonCompactResults <- read.csv("RegularSeasonCompactResults.csv")
DataFiles_RegularSeasonDetailedResults <- read.csv("RegularSeasonDetailedResults.csv")
DataFiles_Seasons <- read.csv("Seasons.csv")
DataFiles_SecondaryTourneyCompactResults <- read.csv("SecondaryTourneyCompactResults.csv")
DataFiles_SecondaryTourneyTeams <- read.csv("SecondaryTourneyTeams.csv")
DataFiles_TeamCoaches <- read.csv("TeamCoaches.csv")
DataFiles_TeamConferences <- read.csv("TeamConferences.csv")
DataFiles_Teams <- read.csv("Teams.csv")
DataFiles_TeamSpellings <- read.csv("TeamSpellings.csv")
### Write ----
if (file.exists(paste(saveDir, "/DataFiles", sep = ""))) {
  setwd(paste(saveDir, "/DataFiles", sep = ""))
} else {
  dir.create(paste(saveDir, "/DataFiles", sep = ""))
  setwd(paste(saveDir, "/DataFiles", sep = ""))
}
saveRDS(DataFiles_Cities, file = "Cities.rds")
saveRDS(DataFiles_Conferences, file = "Conferences.rds")
saveRDS(DataFiles_ConferenceTourneyGames, file = "ConferenceTourneyGames.rds")
saveRDS(DataFiles_GameCities, file = "GameCities.rds")
saveRDS(DataFiles_NCAATourneyCompactResults, file = "NCAATourneyCompactResults.rds")
saveRDS(DataFiles_NCAATourneyDetailedResults, file = "NCAATourneyDetailedResults.rds")
saveRDS(DataFiles_NCAATourneySeedRoundSlots, file = "NCAATourneySeedRoundSlots.rds")
saveRDS(DataFiles_NCAATourneySeeds, file = "NCAATourneySeeds.rds")
saveRDS(DataFiles_NCAATourneySlots, file = "NCAATourneySlots.rds")
saveRDS(DataFiles_RegularSeasonCompactResults, file = "RegularSeasonCompactResults.rds")
saveRDS(DataFiles_SecondaryTourneyTeams, file = "SecondaryTourneyTeams.rds")
saveRDS(DataFiles_TeamCoaches, file = "TeamCoaches.rds")
saveRDS(DataFiles_TeamConferences, file = "TeamConferences.rds")
saveRDS(DataFiles_Teams, file = "Teams.rds")
saveRDS(DataFiles_TeamSpellings, file = "TeamSpellings.rds")

## Massey Ordinals ----
### Read ----
setwd(paste(workingDir, "/MasseyOrdinals", sep = ""))
MasseyOrdinals_MasseyOrdinals <- read.csv("MasseyOrdinals.csv")
### Write ----
if (file.exists(paste(saveDir, "/MasseyOrdinals", sep = ""))) {
  setwd(paste(saveDir, "/MasseyOrdinals", sep = ""))
} else {
  dir.create(paste(saveDir, "/MasseyOrdinals", sep = ""))
  setwd(paste(saveDir, "/MasseyOrdinals", sep = ""))
}
saveRDS(MasseyOrdinals_MasseyOrdinals, file = "MasseyOrdinals.rds")

## Massey Ordinals to mid 2019 ----
### Read ----
setwd(paste(workingDir, "/MasseyOrdinals_thru_2019_day_128", sep = ""))
MasseyOrdinals_MasseyOrdinals_thru_2019_day_128 <- read.csv("MasseyOrdinals_thru_2019_day_128.csv")
### Write ----
if (file.exists(paste(saveDir, "/MasseyOrdinals_thru_2019_day_128", sep = ""))) {
  setwd(paste(saveDir, "/MasseyOrdinals_thru_2019_day_128", sep = ""))
} else {
  dir.create(paste(saveDir, "/MasseyOrdinals_thru_2019_day_128", sep = ""))
  setwd(paste(saveDir, "/MasseyOrdinals_thru_2019_day_128", sep = ""))
}
saveRDS(MasseyOrdinals_MasseyOrdinals, file = "MasseyOrdinals_thru_2019_day_128.rds")

## Play-by-play loop ----
years <- c(2010:2019)
for (i in years) {
  print(paste("Processing", i, "PBP data"))
  setwd(paste(workingDir, "/PlayByPlay_", i, sep = ""))
  ### Read ----
  eventsIter <- paste("Events_", i, sep = "")
  tempEvents <- read.csv(paste("Events_", i, ".csv", sep = ""))
  assign(eventsIter, tempEvents)
  playersIter <- paste("Players_", i, sep = "")
  tempPlayers <- read.csv(paste("Players_", i, ".csv", sep = ""))
  assign(playersIter, tempPlayers)
  ### Write ----
  if (file.exists(paste(saveDir, "/PlayByPlay_", i, sep = ""))) {
    setwd(paste(saveDir, "/PlayByPlay_", i, sep = ""))
  } else {
    dir.create(paste(saveDir, "/PlayByPlay_", i, sep = ""))
    setwd(paste(saveDir, "/PlayByPlay_", i, sep = ""))
  }
  eventsOutTemp = toString(paste("Events_", i, ".rds", sep = ""))
  playersOutTemp = toString(paste("Players_", i, ".rds", sep = ""))
  saveRDS(tempEvents, file = eventsOutTemp)
  saveRDS(tempPlayers, file = playersOutTemp)
}

## Before 2019 Massey Ordinals ----
### Read ----
setwd(paste(workingDir, "/Prelim2019_MasseyOrdinals", sep = ""))
Prelim2019_MasseyOrdinalsMasseyOrdinals <- read.csv("Prelim2019_MasseyOrdinals.csv")
### Write ----
if (file.exists(paste(saveDir, "/Prelim2019_MasseyOrdinals", sep = ""))) {
  setwd(paste(saveDir, "/Prelim2019_MasseyOrdinals", sep = ""))
} else {
  dir.create(paste(saveDir, "/Prelim2019_MasseyOrdinals", sep = ""))
  setwd(paste(saveDir, "/Prelim2019_MasseyOrdinals", sep = ""))
}
saveRDS(Prelim2019_MasseyOrdinalsMasseyOrdinals, file = "Prelim2019_MasseyOrdinals.rds")

## Before 2019 PBP ----
### Read ----
setwd(paste(workingDir, "/Prelim2019_PlayByPlay_2019", sep = ""))
Prelim2019_PlayByPlay_2019Prelim2019_Events_2019 <- read.csv("Prelim2019_Events_2019.csv")
Prelim2019_PlayByPlay_2019Prelim2019_Players_2019 <- read.csv("Prelim2019_Players_2019.csv")
### Write ----
if (file.exists(paste(saveDir, "/Prelim2019_PlayByPlay_2019", sep = ""))) {
  setwd(paste(saveDir, "/Prelim2019_PlayByPlay_2019", sep = ""))
} else {
  dir.create(paste(saveDir, "/Prelim2019_PlayByPlay_2019", sep = ""))
  setwd(paste(saveDir, "/Prelim2019_PlayByPlay_2019", sep = ""))
}
saveRDS(Prelim2019_PlayByPlay_2019Prelim2019_Events_2019, file = "Prelim2019_Events_2019.rds")
saveRDS(Prelim2019_PlayByPlay_2019Prelim2019_Players_2019, file = "Prelim2019_Players_2019.rds")

## Before 2019 Compact Results ----
### Read ----
setwd(paste(workingDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))
MasseyOrdinalsMasseyOrdinals_thru_2019_day_128 <- read.csv("Prelim2019_RegularSeasonCompactResults.csv")
### Write ----
setwd(paste(saveDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))
if (file.exists(paste(saveDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))) {
  setwd(paste(saveDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))
} else {
  dir.create(paste(saveDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))
  setwd(paste(saveDir, "/Prelim2019_RegularSeasonCompactResults", sep = ""))
}
saveRDS(MasseyOrdinalsMasseyOrdinals_thru_2019_day_128, file = "Prelim2019_RegularSeasonCompactResults.rds")

## Stage 2 datafiles ----
### Read ----
setwd(paste(workingDir, "/Stage2DataFiles", sep = ""))
Stage2DataFiles_Cities <- read.csv("Cities.csv")
Stage2DataFiles_Conferences <- read.csv("Conferences.csv")
Stage2DataFiles_ConferenceTourneyGames <- read.csv("ConferenceTourneyGames.csv")
Stage2DataFiles_GameCities <- read.csv("GameCities.csv")
Stage2DataFiles_NCAATourneyCompactResults <- read.csv("NCAATourneyCompactResults.csv")
Stage2DataFiles_NCAATourneyDetailedResults <- read.csv("NCAATourneyDetailedResults.csv")
Stage2DataFiles_NCAATourneySeedRoundSlots <- read.csv("NCAATourneySeedRoundSlots.csv")
Stage2DataFiles_NCAATourneySeeds <- read.csv("NCAATourneySeeds.csv")
Stage2DataFiles_NCAATourneySlots <- read.csv("NCAATourneySlots.csv")
Stage2DataFiles_RegularSeasonCompactResults <- read.csv("RegularSeasonCompactResults.csv")
Stage2DataFiles_RegularSeasonDetailedResults <- read.csv("RegularSeasonDetailedResults.csv")
Stage2DataFiles_Seasons <- read.csv("Seasons.csv")
Stage2DataFiles_SecondaryTourneyCompactResults <- read.csv("SecondaryTourneyCompactResults.csv")
Stage2DataFiles_SecondaryTourneyTeams <- read.csv("SecondaryTourneyTeams.csv")
Stage2DataFiles_TeamCoaches <- read.csv("TeamCoaches.csv")
Stage2DataFiles_TeamConferences <- read.csv("TeamConferences.csv")
Stage2DataFiles_Teams <- read.csv("Teams.csv")
Stage2DataFiles_TeamSpellings <- read.csv("TeamSpellings.csv")
### Write ----
if (file.exists(paste(saveDir, "/Stage2DataFiles", sep = ""))) {
  setwd(paste(saveDir, "/Stage2DataFiles", sep = ""))
} else {
  dir.create(paste(saveDir, "/Stage2DataFiles", sep = ""))
  setwd(paste(saveDir, "/Stage2DataFiles", sep = ""))
}
saveRDS(Stage2DataFiles_Cities, file = "Cities.rds")
saveRDS(Stage2DataFiles_Conferences, file = "Conferences.rds")
saveRDS(Stage2DataFiles_ConferenceTourneyGames, file = "ConferenceTourneyGames.rds")
saveRDS(Stage2DataFiles_GameCities, file = "GameCities.rds")
saveRDS(Stage2DataFiles_NCAATourneyCompactResults, file = "NCAATourneyCompactResults.rds")
saveRDS(Stage2DataFiles_NCAATourneyDetailedResults, file = "NCAATourneyDetailedResults.rds")
saveRDS(Stage2DataFiles_NCAATourneySeedRoundSlots, file = "NCAATourneySeedRoundSlots.rds")
saveRDS(Stage2DataFiles_NCAATourneySeeds, file = "NCAATourneySeeds.rds")
saveRDS(Stage2DataFiles_NCAATourneySlots, file = "NCAATourneySlots.rds")
saveRDS(Stage2DataFiles_RegularSeasonCompactResults, file = "RegularSeasonCompactResults.rds")
saveRDS(Stage2DataFiles_SecondaryTourneyTeams, file = "SecondaryTourneyTeams.rds")
saveRDS(Stage2DataFiles_TeamCoaches, file = "TeamCoaches.rds")
saveRDS(Stage2DataFiles_TeamConferences, file = "TeamConferences.rds")
saveRDS(Stage2DataFiles_Teams, file = "Teams.rds")
saveRDS(Stage2DataFiles_TeamSpellings, file = "TeamSpellings.rds")
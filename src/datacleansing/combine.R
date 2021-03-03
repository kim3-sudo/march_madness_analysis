### March Madness Analysis
### Steven Lucas & Sejin Kim
### STAT 306 S21 @ Kenyon College

# Purpose ----
### This file will grab all of the PBP data from the remote repo
### and create a single R dataset as an export to the directory
### of your choice


# Set your output directory here! ----
outputDir <- "/home/kim3/march_madness_data"

# Get all of the player data from remote repo ----
player2010 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2010/Players_2010.rds?raw=true'))
player2011 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2011/Players_2011.rds?raw=true'))
player2012 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2012/Players_2012.rds?raw=true'))
player2013 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2013/Players_2013.rds?raw=true'))
player2014 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2014/Players_2014.rds?raw=true'))
player2015 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2015/Players_2015.rds?raw=true'))
player2016 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2016/Players_2016.rds?raw=true'))
player2017 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2017/Players_2017.rds?raw=true'))
player2018 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2018/Players_2018.rds?raw=true'))
player2019 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2019/Players_2019.rds?raw=true'))

# Get all of the event data from remote repo ----
events2010 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2010/Events_2010.rds?raw=true'))
events2011 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2011/Events_2011.rds?raw=true'))
events2012 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2012/Events_2012.rds?raw=true'))
events2013 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2013/Events_2013.rds?raw=true'))
events2014 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2014/Events_2014.rds?raw=true'))
events2015 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2015/Events_2015.rds?raw=true'))
events2016 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2016/Events_2016.rds?raw=true'))
events2017 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2017/Events_2017.rds?raw=true'))
events2018 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2018/Events_2018.rds?raw=true'))
events2019 <- readRDS(url('https://github.com/kim3-sudo/march_madness_data/blob/main/PlayByPlay_2019/Events_2019.rds?raw=true'))

# Bind all of the player data ----
players = rbind(player2010, player2011)
players = rbind(players, player2012)
players = rbind(players, player2013)
players = rbind(players, player2014)
players = rbind(players, player2015)
players = rbind(players, player2016)
players = rbind(players, player2017)
players = rbind(players, player2018)
players = rbind(players, player2019)

# Bind all of the event data ----
events = rbind(events2010, events2011)
events = rbind(events, events2012)
events = rbind(events, events2013)
events = rbind(events, events2014)
events = rbind(events, events2015)
events = rbind(events, events2016)
events = rbind(events, events2017)
events = rbind(events, events2018)
events = rbind(events, events2019)

# Proof the data ----
print("Showing the full dataframes")
print("Also printing the heads in the console")
View(players)
View(events)
head(players)
head(events)
if (file.exists(outputDir)) {
  playerOut <- paste(outputDir, "/players.rds", sep = "")
  saveRDS(players, file.path(playerOut))
  eventsOut <- paste(outputDir, "/events.rds", sep = "")
  saveRDS(events, file.path(eventsOut))
} else {
  dir.create(outputDir)
  playerOut <- paste(outputDir, "/players.rds", sep = "")
  saveRDS(players, file.path(playerOut))
  eventsOut <- paste(outputDir, "/events.rds", sep = "")
  saveRDS(events, file.path(eventsOut))
}
print("All done!")

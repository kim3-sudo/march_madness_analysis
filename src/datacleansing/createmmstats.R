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
workingDir = "c:/Users/kim3/Downloads/March-Madness-ML/Data/RegSeasonStats"
saveDir = "c:/Users/kim3/Downloads/March-Madness-ML-RDS/Data/RegSeasonStats"

## Play-by-play loop ----
years <- c(1993:2019)
for (i in years) {
  print(paste("Processing", i, "Reg Season Stats data"))
  setwd(workingDir)
  ### Read ----
  MMStatsIter <- paste("MMStats_", i, sep = "")
  MMStats <- read.csv(paste("MMStats_", i, ".csv", sep = ""))
  assign(MMStatsIter, MMStats)
  ### Write ----
  if (file.exists(saveDir)) {
    setwd(saveDir)
  } else {
    dir.create(saveDir)
    setwd(saveDir)
  }
  MMStatsOutTemp = toString(paste("MMStats_", i, ".rds", sep = ""))
  saveRDS(MMStats, file = MMStatsOutTemp)
}


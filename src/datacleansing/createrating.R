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
workingDir = "c:/Users/kim3/Downloads/March-Madness-ML/Data/RatingStats"
saveDir = "c:/Users/kim3/Downloads/March-Madness-ML-RDS/Data/RatingStats"

## Play-by-play loop ----
years <- c(1993:2019)
for (i in years) {
  print(paste("Processing", i, "Rating Stats data"))
  setwd(workingDir)
  ### Read ----
  ratingStatsIter <- paste("RatingStats_", i, sep = "")
  ratingStats <- read.csv(paste("RatingStats_", i, ".csv", sep = ""))
  assign(ratingStatsIter, ratingStats)
  ### Write ----
  if (file.exists(saveDir)) {
    setwd(saveDir)
  } else {
    dir.create(saveDir)
    setwd(saveDir)
  }
  ratingStatsOutTemp = toString(paste("RatingStats_", i, ".rds", sep = ""))
  saveRDS(ratingStats, file = ratingStatsOutTemp)
}


##### Colley and Massey Rankings for EuroBasket 2018-2019 Regular Season
### Colley Rankings

# Import data
eb2019 <- as.data.frame(read.csv("https://raw.githubusercontent.com/kim3-sudo/march_madness_data/main/2018-2019%20EuroLeague%20Data/2018-2019%20EuroLeague%20Regular%20Season.csv", header=FALSE))
eb2019 <- eb2019[!apply(eb2019 == "", 1, all),]
eb2019 <- na.omit(eb2019)
rownames(eb2019) <- 1:nrow(eb2019)

ebtable <- as.data.frame(read.csv("https://raw.githubusercontent.com/kim3-sudo/march_madness_data/main/2018-2019%20EuroLeague%20Data/2018-2019%20EuroLeague%20Table.csv"))

# Isolate team names and create Colley matrix
names <- ebtable$Team
cmat <- matrix(nrow=length(names), ncol=length(names))
for (i in 1:length(names)) {
  for (j in 1:length(names)) {
    if (i==j) {
      cmat[i,j] <- 2+ebtable$Pld[i]
    } else {
      cmat[i,j] <- -2
    }
  }
}

# Create solution vector and unknown rank vector

ebtable <- ebtable[order(ebtable[,2]),]

bvec <- numeric()
for (i in 1:length(names)) {
  bvec[i] <- 1+(.5*(ebtable$W[i]-ebtable$L[i]))
}

# Solve the linear system to obtain rating values

rvecC <- solve(cmat, bvec)

origcolley <- data.frame("Team" = sort(names), "Place" = ebtable$Pos, "Colley Rating" = rvecC,
                         "Colley Rank" = rank(-1*rvecC, ties.method="min"))

### Massey rankings

# Create Massey matrix and apply nonsigularity correction

names <- ebtable$Team
mmat <- matrix(nrow=length(names), ncol=length(names))
for (i in 1:length(names)) {
  for (j in 1:length(names)) {
    if (i==j) {
      mmat[i,j] <- ebtable$Pld[i]
    } else {
      mmat[i,j] <- -2
    }
  }
}

mmat[length(names),] <- rep(1, times=length(names))

# Create point differential vector and apply nonsingularity correction

pvec <- numeric()
for (i in 1:length(names)) {
  pvec[i] <- ebtable$PF[i]-ebtable$PA[i]
}

pvec[length(names)] <- 0

# Solve the linear system

rvecM <- solve(mmat, pvec)

### Summary of rankings

massrankings <- data.frame("Team" = names, "Place" = ebtable$Pos, 
                       "Massey Rating" = rvecM, "Massey Rank" = rank(-1*rvecM, ties.method="min"))
View(massrankings)

### Massey Rankings with Temporal Weight

# Isolate second half of the season

eb2 <- eb2019[c(121:240),]
rownames(eb2) <- 1:nrow(eb2)

# Calculate points for each team

eb2f <- eb2[order(eb2$V2),]
rownames(eb2f) <- 1:nrow(eb2f)

eb2a <- eb2[order(eb2$V6),]
rownames(eb2a) <- 1:nrow(eb2a)

eb2pts <- data.frame()
for (i in 1:length(names)) {
  eb2pts[i,1] <- sort(names)[i]
  eb2pts[1,2] <- sum(as.numeric(eb2f$V4[1:8]))
  eb2pts[2,2] <- sum(as.numeric(eb2f$V4[9:16]))
  eb2pts[3,2] <- sum(as.numeric(eb2f$V4[17:25]))
  eb2pts[4,2] <- sum(as.numeric(eb2f$V4[26:30]))
  eb2pts[5,2] <- sum(as.numeric(eb2f$V4[31:37]))
  eb2pts[6,2] <- sum(as.numeric(eb2f$V4[38:46]))
  eb2pts[7,2] <- sum(as.numeric(eb2f$V4[47:53]))
  eb2pts[8,2] <- sum(as.numeric(eb2f$V4[54:61]))
  eb2pts[9,2] <- sum(as.numeric(eb2f$V4[62:68]))
  eb2pts[10,2] <- sum(as.numeric(eb2f$V4[69:75]))
  eb2pts[11,2] <- sum(as.numeric(eb2f$V4[76:84]))
  eb2pts[12,2] <- sum(as.numeric(eb2f$V4[85:92]))
  eb2pts[13,2] <- sum(as.numeric(eb2f$V4[93:100]))
  eb2pts[14,2] <- sum(as.numeric(eb2f$V4[101:106]))
  eb2pts[15,2] <- sum(as.numeric(eb2f$V4[107:113]))
  eb2pts[16,2] <- sum(as.numeric(eb2f$V4[114:120]))
  eb2pts[1,3] <- sum(as.numeric(eb2f$V5[1:7]))
  eb2pts[2,3] <- sum(as.numeric(eb2f$V5[8:14]))
  eb2pts[3,3] <- sum(as.numeric(eb2f$V5[15:20]))
  eb2pts[4,3] <- sum(as.numeric(eb2f$V5[21:30]))
  eb2pts[5,3] <- sum(as.numeric(eb2f$V5[31:38]))
  eb2pts[6,3] <- sum(as.numeric(eb2f$V5[39:44]))
  eb2pts[7,3] <- sum(as.numeric(eb2f$V5[45:52]))
  eb2pts[8,3] <- sum(as.numeric(eb2f$V5[53:59]))
  eb2pts[9,3] <- sum(as.numeric(eb2f$V5[60:67]))
  eb2pts[10,3] <- sum(as.numeric(eb2f$V5[68:75]))
  eb2pts[11,3] <- sum(as.numeric(eb2f$V5[76:81]))
  eb2pts[12,3] <- sum(as.numeric(eb2f$V5[82:88]))
  eb2pts[13,3] <- sum(as.numeric(eb2f$V5[89:95]))
  eb2pts[14,3] <- sum(as.numeric(eb2f$V5[96:104]))
  eb2pts[15,3] <- sum(as.numeric(eb2f$V5[105:112]))
  eb2pts[16,3] <- sum(as.numeric(eb2f$V5[113:120]))
  eb2pts[i,4] <- eb2pts[i,2]-eb2pts[i,3]
}

# Create Massey matrix and apply nonsigularity correction

names <- ebtable$Team
mmat2 <- matrix(nrow=length(names), ncol=length(names))
for (i in 1:length(names)) {
  for (j in 1:length(names)) {
    if (i==j) {
      mmat2[i,j] <- 15
    } else {
      mmat2[i,j] <- -1
    }
  }
}

mmat2[length(names),] <- rep(1, times=length(names))

# Create point differential vector and apply nonsingularity correction

pvec2 <- numeric()
for (i in 1:length(names)) {
  pvec2[i] <- eb2pts$V4[i]
}

pvec2[length(names)] <- 0

# Solve the linear system

rvecM2 <- solve(mmat2, pvec2)

mass2 <- data.frame("Team" = names, "Place" = ebtable$Pos,
                    "Massey Rating" = rvecM2, "Massey Rank" = rank(-1*rvecM2, ties.method="min"))

# Import round data for each match, create round vector, and perform log transformation

ebround <- as.data.frame(read.csv("https://raw.githubusercontent.com/kim3-sudo/march_madness_data/main/2018-2019%20EuroLeague%20Data/2018-2019%20EuroLeague%20Round%20Matrix.csv", header=FALSE))
ebround <- ebround[order(ebround[,1]),]
ebround <- ebround[,order(ebround[1,])]
ebround <- ebround[-1,]
ebround <- ebround[,-1]
ebround <- matrix(as.numeric(unlist(ebround)),nrow=nrow(ebround))
ebround <- ebround - matrix(rep(15, times=256), nrow=16, ncol=16)
for (i in 1:nrow(ebround)) {
  ebround[i,i] <- 0
}
wmat <- matrix(nrow=nrow(ebround), ncol=nrow(ebround))
for (i in 1:nrow(ebround)) {
  for (j in 1:nrow(ebround)) {
    wmat[i,j] <- log(1+(ebround[i,j]/15))
  }
}

# Solve the weighted linear system

wrvec <- solve(t(mmat2)%*%wmat%*%mmat2, t(mmat2)%*%wmat%*%pvec2)

wmass <- data.frame("Team" = sort(names),
                    "Weighted Massey Rating" = wrvec,
                    "Weighted Massey Rank" = rank(-1*wrvec, ties.method="min"))

### Colley rankings with binary temporal weighting

cmat2 <- matrix(nrow=length(names), ncol=length(names))
for (i in 1:length(names)) {
  for (j in 1:length(names)) {
    if (i==j) {
      cmat2[i,j] <- 17
    } else {
      cmat2[i,j] <- -1
    }
  }
}

# Construct data.frame for wins and losses in second half of season

for (i in 1:nrow(eb2)) {
  if (i <= 8 && i >= 1) {
    eb2$V1[i] <- 1
  }
  if (i <= (8*2) && i >= (8*1)) {
    eb2$V1[i] <- 2
  }
  if (i <= (8*3) && i >= (8*2)) {
    eb2$V1[i] <- 3
  }
  if (i <= (8*4) && i >= (8*3)) {
    eb2$V1[i] <- 4
  }
  if (i <= (8*5) && i >= (8*4)) {
    eb2$V1[i] <- 5
  }
  if (i <= (8*6) && i >= (8*5)) {
    eb2$V1[i] <- 6
  }
  if (i <= (8*7) && i >= (8*6)) {
    eb2$V1[i] <- 7
  }
  if (i <= (8*8) && i >= (8*7)) {
    eb2$V1[i] <- 8
  }
  if (i <= (8*9) && i >= (8*8)) {
    eb2$V1[i] <- 9
  }
  if (i <= (8*10) && i >= (8*9)) {
    eb2$V1[i] <- 10
  }
  if (i <= (8*11) && i >= (8*10)) {
    eb2$V1[i] <- 11
  }
  if (i <= (8*12) && i >= (8*11)) {
    eb2$V1[i] <- 12
  }
  if (i <= (8*13) && i >= (8*12)) {
    eb2$V1[i] <- 13
  }
  if (i <= (8*14) && i >= (8*13)) {
    eb2$V1[i] <- 14
  }
  if (i <= (8*15) && i >= (8*14)) {
    eb2$V1[i] <- 15
  }
}

eb2wl <- data.frame("Wins" = rep(0, times=length(names)), "Losses" = rep(0, times=length(names)),
                    "Weighted Wins" = rep(0, times=length(names)),
                    "Weighted Losses" = rep(0, times=length(names)))

for (i in 1:nrow(eb2)) {
  if (eb2$V2[i]=="Anadolu Efes" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[1,1] = eb2wl[1,1] + 1
    eb2wl[1,3] = eb2wl[1,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Anadolu Efes" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[1,2] = eb2wl[1,2] + 1
    eb2wl[1,4] = eb2wl[1,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Anadolu Efes" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[1,1] = eb2wl[1,1] + 1
    eb2wl[1,3] = eb2wl[1,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Anadolu Efes" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[1,2] = eb2wl[1,2] + 1
    eb2wl[1,4] = eb2wl[1,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  
  if (eb2$V2[i]=="AX Armani Exchange Olimpia" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[2,1] = eb2wl[2,1] + 1
    eb2wl[2,3] = eb2wl[2,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="AX Armani Exchange Olimpia" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[2,2] = eb2wl[2,2] + 1
    eb2wl[2,4] = eb2wl[2,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="AX Armani Exchange Olimpia" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[2,1] = eb2wl[2,1] + 1
    eb2wl[2,3] = eb2wl[2,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="AX Armani Exchange Olimpia" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[2,2] = eb2wl[2,2] + 1
    eb2wl[2,4] = eb2wl[2,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Barcelona Lassa" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[3,1] = eb2wl[3,1] + 1
    eb2wl[3,3] = eb2wl[3,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Barcelona Lassa" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[3,2] = eb2wl[3,2] + 1
    eb2wl[3,4] = eb2wl[3,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Barcelona Lassa" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[3,1] = eb2wl[3,1] + 1
    eb2wl[3,3] = eb2wl[3,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Barcelona Lassa" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[3,2] = eb2wl[3,2] + 1
    eb2wl[3,4] = eb2wl[3,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Bayern Munich" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[4,1] = eb2wl[4,1] + 1
    eb2wl[4,3] = eb2wl[4,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Bayern Munich" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[4,2] = eb2wl[4,2] + 1
    eb2wl[4,4] = eb2wl[4,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Bayern Munich" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[4,1] = eb2wl[4,1] + 1
    eb2wl[4,3] = eb2wl[4,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Bayern Munich" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[4,2] = eb2wl[4,2] + 1
    eb2wl[4,4] = eb2wl[4,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Budućnost VOLI" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[5,1] = eb2wl[5,1] + 1
    eb2wl[5,3] = eb2wl[5,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Budućnost VOLI" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[5,2] = eb2wl[5,2] + 1
    eb2wl[5,4] = eb2wl[5,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Budućnost VOLI" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[5,1] = eb2wl[5,1] + 1
    eb2wl[5,3] = eb2wl[5,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Budućnost VOLI" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[5,2] = eb2wl[5,2] + 1
    eb2wl[5,4] = eb2wl[5,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="CSKA Moscow" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[6,1] = eb2wl[6,1] + 1
    eb2wl[6,3] = eb2wl[6,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="CSKA Moscow" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[6,2] = eb2wl[6,2] + 1
    eb2wl[6,4] = eb2wl[6,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="CSKA Moscow" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[6,1] = eb2wl[6,1] + 1
    eb2wl[6,3] = eb2wl[6,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="CSKA Moscow" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[6,2] = eb2wl[6,2] + 1
    eb2wl[6,4] = eb2wl[6,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Darüşşafaka Tekfen" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[7,1] = eb2wl[7,1] + 1
    eb2wl[7,3] = eb2wl[7,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Darüşşafaka Tekfen" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[7,2] = eb2wl[7,2] + 1
    eb2wl[7,4] = eb2wl[7,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Darüşşafaka Tekfen" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[7,1] = eb2wl[7,1] + 1
    eb2wl[7,3] = eb2wl[7,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Darüşşafaka Tekfen" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[7,2] = eb2wl[7,2] + 1
    eb2wl[7,4] = eb2wl[7,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Fenerbahçe Beko" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[8,1] = eb2wl[8,1] + 1
    eb2wl[8,3] = eb2wl[8,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Fenerbahçe Beko" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[8,2] = eb2wl[8,2] + 1
    eb2wl[8,4] = eb2wl[8,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Fenerbahçe Beko" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[8,1] = eb2wl[8,1] + 1
    eb2wl[8,3] = eb2wl[8,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Fenerbahçe Beko" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[8,2] = eb2wl[8,2] + 1
    eb2wl[8,4] = eb2wl[8,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Herbalife Gran Canaria" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[9,1] = eb2wl[9,1] + 1
    eb2wl[9,3] = eb2wl[9,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Herbalife Gran Canaria" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[9,2] = eb2wl[9,2] + 1
    eb2wl[9,4] = eb2wl[9,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Herbalife Gran Canaria" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[9,1] = eb2wl[9,1] + 1
    eb2wl[9,3] = eb2wl[9,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Herbalife Gran Canaria" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[9,2] = eb2wl[9,2] + 1
    eb2wl[9,4] = eb2wl[9,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Khimki" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[10,1] = eb2wl[10,1] + 1
    eb2wl[10,3] = eb2wl[10,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Khimki" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[10,2] = eb2wl[10,2] + 1
    eb2wl[10,4] = eb2wl[10,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Khimki" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[10,1] = eb2wl[10,1] + 1
    eb2wl[10,3] = eb2wl[10,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Khimki" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[10,2] = eb2wl[10,2] + 1
    eb2wl[10,4] = eb2wl[10,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Kirolbet Baskonia" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[11,1] = eb2wl[11,1] + 1
    eb2wl[11,3] = eb2wl[11,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Kirolbet Baskonia" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[11,2] = eb2wl[11,2] + 1
    eb2wl[11,4] = eb2wl[11,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Kirolbet Baskonia" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[11,1] = eb2wl[11,1] + 1
    eb2wl[11,3] = eb2wl[11,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Kirolbet Baskonia" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[11,2] = eb2wl[11,2] + 1
    eb2wl[11,4] = eb2wl[11,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Maccabi FOX Tel Aviv" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[12,1] = eb2wl[12,1] + 1
    eb2wl[12,3] = eb2wl[12,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Maccabi FOX Tel Aviv" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[12,2] = eb2wl[12,2] + 1
    eb2wl[12,4] = eb2wl[12,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Maccabi FOX Tel Aviv" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[12,1] = eb2wl[12,1] + 1
    eb2wl[12,3] = eb2wl[12,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Maccabi FOX Tel Aviv" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[12,2] = eb2wl[12,2] + 1
    eb2wl[12,4] = eb2wl[12,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Olympiacos" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[13,1] = eb2wl[13,1] + 1
    eb2wl[13,3] = eb2wl[13,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Olympiacos" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[13,2] = eb2wl[13,2] + 1
    eb2wl[13,4] = eb2wl[13,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Olympiacos" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[13,1] = eb2wl[13,1] + 1
    eb2wl[13,3] = eb2wl[13,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Olympiacos" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[13,2] = eb2wl[13,2] + 1
    eb2wl[13,4] = eb2wl[13,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Panathinaikos OPAP" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[14,1] = eb2wl[14,1] + 1
    eb2wl[14,3] = eb2wl[14,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Panathinaikos OPAP" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[14,2] = eb2wl[14,2] + 1
    eb2wl[14,4] = eb2wl[14,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Panathinaikos OPAP" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[14,1] = eb2wl[14,1] + 1
    eb2wl[14,3] = eb2wl[14,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Panathinaikos OPAP" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[14,2] = eb2wl[14,2] + 1
    eb2wl[14,4] = eb2wl[14,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Real Madrid" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[15,1] = eb2wl[15,1] + 1
    eb2wl[15,3] = eb2wl[15,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Real Madrid" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[15,2] = eb2wl[15,2] + 1
    eb2wl[15,4] = eb2wl[15,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Real Madrid" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[15,1] = eb2wl[15,1] + 1
    eb2wl[15,3] = eb2wl[15,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Real Madrid" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[15,2] = eb2wl[15,2] + 1
    eb2wl[15,4] = eb2wl[15,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  
  if (eb2$V2[i]=="Žalgiris" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[16,1] = eb2wl[16,1] + 1
    eb2wl[16,3] = eb2wl[16,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V2[i]=="Žalgiris" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[16,2] = eb2wl[16,2] + 1
    eb2wl[16,4] = eb2wl[16,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Žalgiris" && eb2$V4[i]<eb2$V5[i]) {
    eb2wl[16,1] = eb2wl[16,1] + 1
    eb2wl[16,3] = eb2wl[16,3] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
  if (eb2$V6[i]=="Žalgiris" && eb2$V4[i]>eb2$V5[i]) {
    eb2wl[16,2] = eb2wl[16,2] + 1
    eb2wl[16,4] = eb2wl[16,4] + (log(1+(as.numeric(eb2$V1[i])/15)))
  }
}

bvec2 <- numeric()
for (i in 1:length(names)) {
  bvec2[i] <- 1+(.5*(eb2wl$Wins[i]-eb2wl$Losses[i]))
}

rvecc2 <- solve(cmat2, bvec2)

colley2 <- data.frame("Team" = sort(names), "Place" = ebtable$Pos,
                    "Binary Weighted Colley Rating" = rvecc2,
                    "Binary Weighted Colley Rank" = rank(-1*rvecc2, ties.method="min"))

### Colley ratings with logarithmic temporal weighting

wcmat2 <- matrix(nrow=length(names), ncol=length(names))
for (i in 1:length(names)) {
  for (j in 1:length(names)) {
    if (i==j) {
      wcmat2[i,j] <- 2+sum(wmat[,i])
    } else {
      wcmat2[i,j] <- -1*wmat[i,j]
    }
  }
}

wbvec2 <- rep(0, times = length(names))
for (i in 1:length(names)) {
  wbvec2[i] <- 1+(.5*(eb2wl$Weighted.Wins[i]-eb2wl$Weighted.Losses[i]))
}

wcrvec2 <- solve(wcmat2, wbvec2)

colleyw <- data.frame("Team" = names,"Place" = ebtable$Pos, "Weighted Colley Rating" = wcrvec2,
                      "Weighted Colley Rank" = rank(-1*wcrvec2, ties.method="min"))

rveccw <- solve(t(cmat2)%*%wmat%*%cmat2, t(cmat2)%*%wmat%*%bvec2)


finalrank <- data.frame("Team" = names, "Place" = ebtable$Pos, "Weighted Colley Rating" = rveccw,
                        "Weighted Colley Rank" = rank(-1*rveccw, ties.method="min"),
                        "Weighted Massey Rating" = wrvec,
                        "Weighted Massey Rank" = rank(-1*wrvec, ties.method="min"),
                        "WCR1" = wcrvec2, "WCR2" = rank(-1*wcrvec2, ties.method="min"))




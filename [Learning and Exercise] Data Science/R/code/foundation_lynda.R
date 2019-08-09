2+2
1:100

#1. x assignment:
x<-1:5 
x #[1] 1 2 3 4 5

#2. y assignment:
y <- c(6,7,8,9,10) # load data into a vector using the "c"ombine function
y <- a(16,7,8,9,10) #Error in a(16, 7, 8, 9, 10) : could not find function "a"
y #[1]  6  7  8  9 10

#3. x+y:
x+y #7  9 11 13 15

y<-c(10,11,12,13)
y #10 11 12 13
x+y # Warning: In x + y : longer object length is not a multiple of shorter object length

#4. List objects
ls() #"x" "y"

#----------------------------
#5. Read from csv:
testname <- read.csv("C:\\Learning\\R\\material\\Exercise_Files\\Ch03\\03_01\\social_network.csv")
testname

#header: 1st line as header or not, logical
testname <- read.csv("C:\\Learning\\R\\material\\Exercise_Files\\Ch03\\03_01\\social_network.csv", header=T)
testname

#OR:
testname2 <- read.csv("C:/Learning/R/material/Exercise_Files/Ch03/03_01/social_network.csv", header=T)
testname2
str(testname2) #Get the type, column, values.
#----------------------------
#6. Rename, library and convert to dataframe:
install.packages('foreign')
library(foreign)
sn.sav.csv <- read.spss("C:/Learning/R/material/Exercise_Files/Ch03/03_01/social_network.sav", header=T, to.data.frame = T, use.value.labels = T)
sn.sav.csv

#-------------------------------
#7. library/package:
browseURL("http://cran.r-project.org/web/views")
browseURL("https://cran.r-project.org/web/packages/available_packages_by_name.html")
library() #Bring up editor list of available packages
search() #Show current active packages

install.packages('psych') #Download the package from CRAM and install in R;
library('psych') #Make package available; Preferred for loading in scripts
require('psych') #Preferred for loading in functions and packages
library(help='psych') #bring up window to show the help

vignette(package='psych') #bring up list of all vignettes
browseVignettes(package='psych') #bring up browser for all vignettes

update.packages()#update the packages

#-----------------------------------
#-----------------------------------
#8. Create the bar charts for categorial variables
sn <- read.csv("C:\\Learning\\R\\material\\Exercise_Files\\Ch03\\03_01\\social_network.csv", header=T)
sn

# R doesn't create the bar charts directly from the categorial variables, 
# thus, we have to create a table that has the frequencies for each level of variable.
# The 'table' function is to create the table from the variable, which we specify as 'sn$Site'.
# That is: we first give the <name of the dataframe>, then $, then <the name of the variable>.

site.freq <- table(sn$Site)
barplot(site.freq) # Create barplots in new window.
? barplot #help in more info.

barplot(site.freq[order(site.freq, decreasing = T)]) # put the bars in descending order by 'order()'.
barplot(site.freq[order(site.freq)], horiz = T) # Draw the bars horizontally, but turn off the decreasing.

#Color:
fbba <- c(rep('gray', 5), rgb(59,89,190, maxColorValue = 255)) #Define the color. rep(a, n): repeat a for n times.
barplot(site.freq[order(site.freq)], horiz = T, col = fbba) #Color the top 1 into blue.

# Plot with more parameters:
barplot(site.freq[order(site.freq)],
        horiz = T,
        col = fbba,
        xlim = c(0,100), #Scale from 0-100
        border = F,
        main = 'Preferred social networking site\nA Survey of 202 Users',
        xlab = 'Number of Users')

# histogram:
hist(sn$Age)
hist(sn$Age, 
     col = colors()[18], #Or use: col = 'beige'
     main = 'Ages of Respondents\nSocial Networking Survey of 202 Users',
     xlab = 'Age of Respondents') # xlabel

# colors:
colors()[19]
colors()[c(44,126,34)] #Color names

#----------------------------------
# 9. Boxplot:
boxplot(sn$Age)
boxplot(sn$Age,
        col='beige',
        notch=T,
        horizontal = T,
        main='Ages of Respondents\nSocial Networking Survey of 202 Users',
        xlab = 'Age of Respondents')
#---------------------------------
# 10. Calculate frequency:
sn <- read.csv('C:\\Learning\\R\\material\\Exercise_Files\\Ch03\\03_01\\social_network.csv', header = T)
site.freq <- table(sn$Site) # Save the Site information to table.
str(site.freq) #structure: 'table' int 
site.freq # Print out the frequencies of every sites by integers.

site.freq <- site.freq[order(site.freq, decreasing = T)]# Sorted decreasingly.
site.freq
#---------------------------------
#11. Caculate proportions:
site.prop <- prop.table(site.freq) # Give proportions of total
site.prop

round(prop.table(site.freq), 2) # Round to 2 decimals.

#------------------------------------
#12. Caculate descriptive:
summary(sn$Age) # Summary on some column of table
summary(sn)

fivenum(sn$Age)
#------------------------------------
#13. describe the table: 
describe(sn)

install.packages('psych')
library('psych')
describe(sn)
#-------------------------------------
#14. Recoding variables:
hist(sn$Times)
describe(sn$Times)

times.z <- scale(sn$Times) #z.score: user built-in function 'scale'
hist(times.z)
describe(times.z)

times.log <- log(sn$Times) #log: will be wrong if undefined logs for 0 times
hist(times.log)
describe(times.log) 

#solution to last error if 0 times:
times.ln1 <- log(sn$Times+1)
hist(times.ln1)
describe((times.ln1))

#--------------------------------------
#15. Ranking:
times.rank <- rank(sn$Times) #Returns the sample ranks of the values in a vector. Ties (i.e., equal values) and missing values can be handled in several ways.
hist(times.rank)
describe(times.rank)

times.rankr <- rank(sn$Times, ties.method = 'random')
hist(times.rankr)
describe(times.rankr)
#------------------------------------
#16. if else:
time.gt1 <- ifelse(sn$Times > 1,'yes',0) #time.gt1 means: if the time>greater than 1: If sn$Times>1, then time.gt1<-'yes'; else time.gt1<-0;
time.gt1

#----------------------------------------
#17. random picking and distribution:
n1 <- rnorm(1000) # n1: with 1000 random normal values;
n2 <- rnorm(1000) # n2: with 1000 random normal values;

hist(n1)
hist(n2)

#17.1. values add:
n.add <- n1+n2 
hist(n.add)

n.multi <- n1*n2
hist(n.multi)

#---------------------------------------
#18. kurtosis() in psych lib:
install.packages('psych')
library('psych')

hist(n1)
kurtosi(n1)

hist(n2)
kurtosi(n2)

hist(n.add)
kurtosi(n.add)

hist(n.multi)
kurtosi(n.multi)
#the excess kurtosis describes the tail shape of the data distribution. The normal distribution has zero excess kurtosis and thus the standard tail shape.

#-----------------------------------------
#19. Create charts for group distributions:
google <- read.csv('C:/Learning/R/code/data/google_correlate.csv', header=T)
str(google)
names(google) # column names

# Split by categories and show the distributions:
viz.reg.dist <- split(google$data_viz, google$region) # Split data by region, create new df.
boxplot(viz.reg.dist, col='lavender') #boxplot by region

#---------------------------------------------
#20. mean of some column:
viz.reg.mean <- sapply(viz.reg.dist, mean)
barplot(viz.reg.mean, 
        col='beige', 
        main='Average Google search share of \n\'data visualization\' by Region of US')
abline(h=-0.1)
abline(h=0)
abline(h=0.1)

#-----------------------------------------------
#21. print info by columns:
describeBy(google$data_viz, google$region)

#----------------------------------------------
#22. plot by 2 variables:
plot(google$degree, google$data_viz) #Basic plot; x, y.
plot(google$degree, google$data_viz, 
     main='Interest in Data visualization Searches\n by percent of population with college degrees',
     xlab = 'Population with college degress',
     ylab = 'Search for \'data visualization\'', 
     pch = 3, # The different points symbols 
     col = 'grey') 
#----------------------------------------------
#23. Fit lines:

#23.1 Linear regression line(y~x):
abline(lm(google$data_viz~google$degree), col='red') #abline(lm(y ~ X), col='red')

#23.2 Lowess smoother line(x,y):
lines(lowess(google$data_viz ~ google$degree), col='blue') #lines(lowess(X, y)) OR lines(lowess(y~X))

#-----------------------------------------------
#24. quantities of variables patterns:
pairs(~data_viz+google$degree+google$facebook+google$nba,
      data = google,
      pch=20,
      main='simple Scatterplot Matrix')
library('psych')
pairs.panels(google[c(3,7,4,5)], gap=0) #google[c(3,7,4,5)]: The column of ds.

#-------------------------------------------------
#25. 3D Scatter plot:
install.packages('rgl') # The rgl package is used to produce interactive 3-D plots.
library('rgl')

plot3d(google$data_viz, # x variable
       google$degree, # y variable
       google$facebook, #z variable
       xlab='data_viz',
       ylab='degree',
       zlab = 'facebook',
       col='red',
       size=3
       )
#---------------------------------------------------
#26. Quantity variables correlation matrix:
g.quant <- google[c(3,7,4,5)]
cor(g.quant)
head(g.quant)

cor.test(g.quant$data_viz, g.quant$degree) # Test 1 pair of variables at a time
#----------------------------------------------------
#27. p-values:
install.packages("Himsc")
library('Himsc') # Himsc to get p-values for matrix.

rcorr(as.matrix(g.quant)) #Coerce g.quant from df to matrix.Then get correlation matrix & p-values.

#----------------------------------------------------
#28. Linear model to predict:
names(google)
reg1 <- lm(data_viz ~ degree + stats_ed + region + facebook + nba,
           data = google) # Predict by linear model, and predictors by '+'.
summary(reg1) #Have to get the result listed by 'summary()'

#-----------------------------------------------------
#29. Marginal frequencies:
sn.tab <- table(sn$Gender, sn$Site)
sn.tab

margin.table(sn.tab, 1) #Row marginal frequencies
margin.table(sn.tab, 2) #Column marginal frequencies

prop.table(sn.tab)
round(prop.table(sn.tab), 2) #cell %

round(prop.table(sn.tab, 1), 2) #row %
round(prop.table(sn.tab, 2), 2) #column %

round(prop.table(sn.tab, 1), 1)  
round(prop.table(sn.tab, 2), 1) 

#----------------------------------------------------
#30. Chi-squared test:
chisq.test(sn.tab)

#-------------------------------------------------
#31. Independent 2-group t-test:
# T-test is the common inferential test to compare 2 groups on a single quantitative outcome.
t.test(google$nba, google$hasnba)

#-----------------------------------------------------
#32. Comparing multiple groups by single variable, with ANOVA
anoval <- aov(data_viz ~ region, data = google)
summary(anoval)

# 2 ways for factorial design:
# I. + and interaction:
anova2a <- aov(data_viz ~ region + stats_ed + region:stats_ed,
              data=google)
summary(anova2a)

#II. *:
anova2b <- aov(data_viz ~ region*stats_ed,
               data=google)
summary(anova2b)


anova2c <- aov(data_viz ~ stats_ed * region,
               data=google) #Diff
summary(anova2c)


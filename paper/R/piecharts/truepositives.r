# Create Data
# ch new 2 dup 1
# v8 new 1 dup 0
# jsc new 5 dup 0
# sm new 0 dup 2
true_positive_perc=c(9,2)
true_positive_names=c("Bug","Duplicate")

labs <- paste(true_positive_names, " (", true_positive_perc, ")", sep="")

pie(true_positive_perc , labels=labs, radius=.5, cex=1.2)
# Create Data
# v8
# jsc 14
# sm
# ch
false_positive_perc=c(1,3,9,1)
false_positive_names=c("Unknown","Timeout/OME", "Undefined", "Not Implemented")
labs <- paste(false_positive_names, " (", false_positive_perc, ")", sep="")
pie(false_positive_perc, labels=labs, radius=.5, cex=1.3)
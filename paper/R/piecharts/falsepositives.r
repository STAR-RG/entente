# Create Data
false_positive_perc=c(9,3,9,5)
false_positive_names=c("Unknown","Timeout/OME", "Undefined", "Not Implemented")
labs <- paste(false_positive_names, " (", false_positive_perc, ")", sep="")
pie(false_positive_perc, labels=labs, radius=.5, cex=1.3)
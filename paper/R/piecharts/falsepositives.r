# Create Data
false_positive_perc=c(4,3,9,2)
false_positive_names=c("Unknown","Timeout/OME", "Undefined", "Not Implemented")
labs <- paste(false_positive_names, " (", false_positive_perc, ")", sep="")
pie(false_positive_perc, labels=labs, radius=.5, cex=1.3)
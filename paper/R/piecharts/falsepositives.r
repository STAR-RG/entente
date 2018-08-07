# Create Data
false_positive_perc=c(0,2,0,0,5,2)
false_positive_names=c("Not Implemented","Timeout/OME", "Undefined", "Future", "Error Message Mismatch", "Invalid Test case")
labs <- paste(false_positive_names, " (", false_positive_perc, ")", sep="")
pie(false_positive_perc, labels=labs, radius=.5, cex=1.3)
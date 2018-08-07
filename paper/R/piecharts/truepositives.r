# Create Data
true_positive_perc=c(5,1)
true_positive_names=c("Bug","Duplicate")

labs <- paste(true_positive_names, " (", true_positive_perc, ")", sep="")

pie(true_positive_perc , labels=labs, radius=.5, cex=1.2)
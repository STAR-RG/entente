# Stacked Bar Plot with Colors and Legend

table <- read.table("stacked.data", header = TRUE, sep = "", quote = "\"")
counts <- table(table$Status, table$Engine)
#col=c("darkblue","red"), 
barplot(counts, xlab="Engine", legend = rownames(counts)) 
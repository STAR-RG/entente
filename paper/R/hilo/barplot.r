# Grouped Bar Plot
table <- read.table("warnings.data", header = TRUE, sep = ",", quote = "\"")

counts <- table(table$category, table$fuzzer)

densities = c(15, 10)
angles = c(45, 145)

barplot(counts, main="",
  xlab="", ylab="Number of warnings", col=c("darkblue","red"),
  legend = rownames(counts),  
  beside=TRUE, angle=angles, density=densities, cex.lab=2, cex.axis=2, cex.names=2, cex=2, args.legend=c(cex=1.15))

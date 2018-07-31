par(mfrow=c(3,2), mar=c(1,3,2,1))

# , oma=c(2,2,2,2)
#, mai = c(1, 1, 1, 1)

## nofuzz
table <- read.table("nofuzz-lo.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="nofuzz [lo]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

table <- read.table("nofuzz-hi.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="nofuzz [hi]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

## radamsa
table <- read.table("radamsa-lo.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="radamsa [lo]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

table <- read.table("radamsa-hi.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="radamsa [hi]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

## quickfuzz
table <- read.table("quickfuzz-lo.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="quickfuzz [lo]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

table <- read.table("quickfuzz-hi.data", header = TRUE, sep = ",", quote = "\"")
barplot(sort(table$num, decreasing=TRUE), main="quickfuzz [hi]", xlab="",
beside=TRUE, angle=angles, cex.lab=2, cex.axis=2, cex.names=2, cex=2,
args.legend=c(cex=1.15))

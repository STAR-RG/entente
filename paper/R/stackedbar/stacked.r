library(ggplot2)

table <- read.table("stacked.data", header = TRUE, sep = "", quote = "\"")
counts <- table(table$Status, table$Engine)

vector <- c(counts["Confirmed","Chakra"],
            counts["Confirmed","JavaScriptCore"],
            counts["Confirmed","V8"],
            counts["Fixed","Chakra"],
            counts["Fixed","JavaScriptCore"],
            counts["Fixed","V8"],
            counts["New","Chakra"],
            counts["New","JavaScriptCore"],
            counts["New","V8"])

df <- data.frame(status=rep(c("Confirmed", "Fixed", "New"), each=3),
                 engine=rep(c("Chakra", "JavaScriptCore", "V8"), each=1),
                 number=vector)

ggplot(data=df, aes(x=engine, y=number, fill=status)) +
  geom_bar(stat="identity")  +
  scale_fill_grey(start = 0, end = .9) + 
  theme_bw() +
  theme(axis.text=element_text(size=14), axis.title.x=element_blank(), axis.title.y=element_blank(), legend.text=element_text(size=14), aspect.ratio=0.5, panel.border = element_blank())



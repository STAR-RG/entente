library(ggplot2)

table <- read.table("/home/jefferson/Documentos/PPGCC UFPA/PESQUISA (Prof. Gustavo)/jsengines-differential-testing/paper/R/stackedbar/stacked.data", header = TRUE, sep = "", quote = "\"")
counts <- table(table$Status, table$Source)

vector <- c(counts["2-Confirmed","Trans"],
            counts["2-Confirmed","Diff"],
            counts["3-Fixed","Trans"],
            counts["3-Fixed","Diff"],
            counts["1-New","Trans"],
            counts["1-New","Diff"])

df <- data.frame(status=rep(c("2-Confirmed", "3-Fixed", "1-New"), each=2),
                 engine=rep(c("Trans", "Diff"), each=1),
                 number=vector)

ggplot(data=df, aes(x=engine, y=number, fill=status)) +
  geom_bar(stat="identity")  +
  scale_fill_grey(start = 0, end = .9) + 
  theme_bw() +
  theme(axis.text=element_text(size=14), axis.title.x=element_blank(), axis.title.y=element_blank(), legend.text=element_text(size=14), aspect.ratio=0.3, panel.border = element_blank())



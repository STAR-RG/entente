NAME:=paper

OLD:=SQJ/old_version.tex
NEW:=new_version.tex
DIFFNAME:=diff

# To update, run: latex-process-inputs -makefilelist main.tex
TEX_FILES = \
paper.tex 

pdf:
#	-rm -f $(NAME).aux
	latexmk -pdf $(NAME)

final: pdf
	@echo '******** Did you spell-check the paper? ********'
	pdffonts $(NAME).pdf; fi

clean:
	-rm -f *aux *bbl *blg *log *.dvi $(NAME).pdf $(NAME).fdb_latexmk $(NAME).fls $(NAME).out
	-rm -f *aux *bbl *blg *log *.dvi $(DIFFNAME).pdf $(DIFFNAME).fdb_latexmk $(DIFFNAME).fls $(DIFFNAME).out $(NEW) $(DIFFNAME).pdf $(DIFFNAME).tex

diff:
	latexpand $(NAME).tex > $(NEW)
	latexdiff $(OLD) $(NEW) > $(DIFFNAME).tex
	latexmk -pdf $(DIFFNAME)

tags: TAGS
TAGS: ${TEX_FILES}
	etags ${TEX_FILES}

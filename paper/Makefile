NAME:=paper

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

tags: TAGS
TAGS: ${TEX_FILES}
	etags ${TEX_FILES}

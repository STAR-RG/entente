FILE=main

pdf:
	pdflatex $(FILE).tex
	bibtex $(FILE)
	pdflatex $(FILE).tex
	pdflatex $(FILE).tex

proposal: pdf
	-@(pdftk main.pdf damorim-cv-red.pdf cat output proposal.pdf)

clean:
	-@(touch main.toc main.ps main.pdf main.dvi main.aux main.bbl main.log main.blg)
	-@(rm *.ps *.toc *.dvi *.aux *.blg *.bbl *.log)

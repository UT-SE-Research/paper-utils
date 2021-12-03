NAME := main
TEXS := $(wildcard *.tex)
TABLES := $(wildcard tables/*.tex)
BIBS := $(wildcard *.bib)

%.pdf: %.fig
	fig2dev -L eps -f Roman $*.fig >$*.eps

all: ${NAME}.pdf

${NAME}.pdf: ${TEXS} ${TABLES} ${BIBS}
	#-rm -f ${NAME}.aux
	#-rm -f ${NAME}.bbl
	-pdflatex $(NAME) && bibtex $(NAME) && pdflatex $(NAME) && bibtex $(NAME) && pdflatex $(NAME)
	@echo '****************************************************************'
	#@latex $(NAME) | grep -E 'arning|erfull'
	#@pdflatex $(NAME) | grep -E 'arning|erfull'
	#@dvipdfm -p letter $(NAME)
	#dvips -t letter -o $(NAME).ps $(NAME).dvi
	#ps2pdf -dPDFSETTINGS=/prepress $(NAME).ps $(NAME).pdf
	@echo '******** Did you spell-check the paper? ********'

clean:
	ls $(NAME)* | grep -v ".tex" | xargs rm -f
	rm -f *.bak *~

PD=pandoc

all: pres.html

pres.html: pres.md
	# $(PD) -t revealjs --katex --embed-resources --standalone --slide-level=3 pres.md -o pres.html
	$(PD) -t revealjs --katex --standalone --slide-level=3 pres.md -o pres.html

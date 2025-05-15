PD=pandoc

all: pres.html

pres.html: pres.md
	$(PD) -t revealjs -s --slide-level=2 pres.md -o pres.html -V revealjs-url=https://unpkg.com/reveal.js@^4

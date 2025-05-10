.PHONY: venv

VENV=.venv

venv:
	python -m venv $(VENV)
	. $(VENV)/bin/activate ; pip install -U manim-slides[manim]

pres.html: main.py
	. $(VENV)/bin/activate ; manim -qk main.py Presentation && manim-slides convert Presentation pres.html --open --one-file --offline -cprogress=true

clean:
	rm -rf $(VENV)

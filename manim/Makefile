.PHONY: clean

VENV=.venv

$(VENV):
	python -m venv $(VENV)
	. $(VENV)/bin/activate
	pip install -U manim-slides[manim]

crypto.html: crypto.py $(VENV)
	. $(VENV)/bin/activate
	manim-slides render crypto.py PresentationCrypto && manim-slides convert PresentationCrypto crypto.html --open --one-file --offline -cprogress=true

clean:
	rm -rf $(VENV)

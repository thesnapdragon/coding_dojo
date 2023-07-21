PLANTUMLS := $(wildcard *.plantuml)
PNGS := $(PLANTUMLS:.plantuml=.png)

$(PNGS): $(PLANTUMLS)
	python -m plantuml $?
	@touch $?

$(PLANTUMLS): requirements.txt
	pip install -r requirements.txt

.PHONY: clean
clean:
	-rm *.png

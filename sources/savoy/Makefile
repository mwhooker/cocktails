SOURCES=$(wildcard *.jpg)
OBJECTS=$(SOURCES:.jpg=.txt)

.PHONY=doocr

doocr: $(OBJECTS)

%.txt : %.jpg
	@tesseract $< $(@:.txt=) -l eng

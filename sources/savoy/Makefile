SOURCES=$(wildcard *.jpg)
OBJECTS=$(SOURCES:.jpg=.txt)

.PHONY=doocr


%.txt : %.jpg
	tesseract $< $(@:.txt=)

doocr: $(OBJECTS)


nothing:
	$(foreach img,$(SOURCES),$(shell tesseract $(img) $(img:.jpg=)))
	tesseract $(patsubst %.txt,%.jpg,$@) $(patsubst %.txt, $@:.txt=)
	$(patsubst %.txt,%.jpg,$@)

SOURCES=$(wildcard *.jpg)
OBJECTS=$(SOURCES:.jpg=.txt)

.PHONY=doocr

doocr: $(OBJECTS)

%.tif : %.jpg
	/Applications/GIMP.app/Contents/MacOS/GIMP -i -b '(simple-antialias "$(abspath $<)"  "$(abspath $(@:.jpg=.tiff))")' -b '(gimp-quit 0)'

%.txt : %.tif
	@tesseract $< $(@:.txt=) -l eng

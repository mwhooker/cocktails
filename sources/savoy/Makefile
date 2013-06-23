SOURCES=$(wildcard *.jpg)
OBJECTS=$(SOURCES:.jpg=.txt)
TIFS=$(SOURCES:.jpg=.tif)

.PHONY=doocr

doocr: $(OBJECTS)

%.tif : %.jpg
	/Applications/GIMP.app/Contents/MacOS/GIMP -i -b '(simple-antialias "$(abspath $<)"  "$(abspath $(@:.jpg=.tiff))")' -b '(gimp-quit 0)'

%.txt : %.tif
	@tesseract $< $(@:.txt=) -l eng

clean:
	@rm $(OBJECTS)

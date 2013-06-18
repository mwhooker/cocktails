#!/bin/bash

inputs=`ls eng.savoy.exp*.png`

for i in $inputs; do
    tesseract $i ${$i%.*} box.train;
done
unicharset_extractor *.box
shapeclustering -F font_properties -U unicharset eng.savoy.exp*.tr
mftraining -F font_properties -U unicharset -O lang.unicharset eng.savoy.exp*.tr
cntraining eng.savoy.exp*.tr
combine_tessdata eng.

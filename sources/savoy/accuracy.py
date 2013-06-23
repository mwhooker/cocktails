#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import Levenshtein
from subprocess import call


"""
http://www.cra.org/Activities/craw_archive/dmp/awards/2008/Elmore/melmore_dmp.pdf


To determine the accuracy of the recognition, we used the
metric proposed by the Information Science Research Institute at UNLV for the
Fourth Annual Test of OCR Accuracy
[23]. If n is the ground truth number of text characters in
the image, and m is the number of errors, or edit operations
(insert, delete, and substitute) needed to transform the result from the OCR
engine into the actual text in the image,
the accuracy of the recognition is deﬁned as (n - m) / n
The upper bound on this metric is 100, a perfect recognition;
there is no lower bound, as negative scores are possible when
there are more errors than characters in the ground truth
text of the image.
To calculate the accuracy for each test image, we used the
accuracy program provided in the OCR Frontiers Toolkit,
the companion software to the ISRI’s 1999 book on OCR
[24]. This toolkit is provided with Tesseract OCR to be
used in evaluating one’s build of the Tesseract system
"""

def score(inp):
    with open('286-corrected.txt') as f:
        truth_file = f.read()

    with open(inp) as f:
        test_file = f.read()

    n = len(truth_file)
    m = Levenshtein.distance(truth_file, test_file)

    return ((n - m) / n)

def runtest():
    outfile = '286tiff'
    cmd = "tesseract 286.tif {outfile} -l eng".format(outfile=outfile)
    call(cmd.split())
    return score(outfile + '.txt')


if __name__ == '__main__':
    print(score(sys.argv[1]))

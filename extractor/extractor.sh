#!/usr/bin/env bash

convert -density 300 $1 -depth 8 -strip -background white -alpha off tempconvert.tiff
tesseract tempconvert.tiff $1
rm tempconvert.tiff
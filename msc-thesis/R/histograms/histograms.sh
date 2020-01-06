#!/bin/bash

name="histograms"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

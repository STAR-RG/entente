#!/bin/bash

name="stacked-engine"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

name="stacked-technique"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

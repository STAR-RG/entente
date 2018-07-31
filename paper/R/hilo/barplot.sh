#!/bin/bash

name="barplot"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

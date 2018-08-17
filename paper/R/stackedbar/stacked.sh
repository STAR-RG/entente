#!/bin/bash

name="stacked"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

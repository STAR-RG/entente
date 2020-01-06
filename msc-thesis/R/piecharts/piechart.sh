#!/bin/bash

name="falsepositives"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

name="truepositives"
Rscript --vanilla ${name}.r 
mv Rplots.pdf ${name}.pdf

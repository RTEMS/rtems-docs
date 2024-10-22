#!/bin/sh -x
mogrify -path _static/ -format ico -density 150 -background none -define icon:auto-resize=48,32,16 favicon.svg
mogrify -path _static/ -format ico -density 150 -background none -define icon:auto-resize=48,32,16 favicon_docs.svg

#!/bin/bash

zcat *.gz | cut --output-delimiter="," -c16-23,24-27,88-92 | cut --output-delimiter="." -c1-18,19 | grep -v "+9999" | sort > ../data.csv
gzip ../data.csv


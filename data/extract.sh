#!/bin/bash

zcat *.gz | cut --output-delimiter="," -c16-27,88-92 | grep -v "+9999" | cut --output-delimiter="." -c1-17,18 | sort > ../data.csv
gzip -f ../data.csv


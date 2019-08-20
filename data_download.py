#!/usr/bin/env python
import sh
import sys
import os
import glob
from optparse import OptionParser

def get_files(usaf, wban):
	output = sh.grep("%s %s" %(usaf, wban), "isd-history.txt").strip().split(" ")
	end = int(output.pop()[0:4])
	start = int(output.pop()[0:4])
	sh.mkdir("-p", "%s-%s" % (usaf, wban))
	os.chdir("%s-%s" % (usaf, wban))
	for year in range(start, end+1):
		fn = "%s-%s-%s.gz" % (usaf, wban, year)
		if not os.path.exists(fn):
			sh.wget("ftp://ftp.ncdc.noaa.gov/pub/data/noaa/%s/%s" % (year, fn))
			print(fn)
	output_fn = "%s-%s-data.csv" %(usaf, wban)
	h = open(output_fn, "w")
	sh.sort(
		sh.cut(
			sh.cut(
				sh.grep(
					sh.zcat(glob.glob("*.gz")),
					"-v", "+9999"),
				"--output-delimiter=,", "-c16-27,88-92"),
			"--output-delimiter=.", "-c1-17,18"),
		_out=h)
	sh.gzip(output_fn)
	sh.mv("%s.gz" % (output_fn), "..")


def option_parser():
	usage = "usage: %prog [name]"
	parser = OptionParser(usage=usage)
	return parser

def main():
	parser = option_parser()
	(options, args) = parser.parse_args()
	if len(args) != 2:
		sys.stderr.write("requires both USAF and WBAN as args\n")
		sys.exit(1)
	get_files(args[0], args[1])

if __name__ == '__main__':
	main()


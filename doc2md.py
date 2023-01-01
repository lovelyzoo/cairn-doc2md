import argparse
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import re

# TODO:
# Input file as parameter
# Output file as parameter
# Get title from start of file
# Make preamble optional

preamble = '''---
layout: default
parent: Conversions
grand_parent: Adventures
title: Through Ultan's Door One
---


# '''

if __name__ == "__main__":

	parser = argparse.ArgumentParser(
                    prog = 'doc2md',
                    description = 'Converts a google doc, exported as an html file, to markdown')
	
	parser.add_argument('infile')
	
	args = parser.parse_args()
	
	# Read the html file into bs4 object
	with open(args.infile, 'r') as f:
		soup = BeautifulSoup(f.read(), 'html.parser')

	# remove the style element
	soup.find('style').clear()
	  
	# convert html to markdown
	as_md = md(str(soup), heading_style="SETEXT", strip=['hr'], bullets = '-')
	
	with open('TUD_one.md', 'w') as f:
		f.write(preamble)

		for line in as_md.splitlines():
			f.write(re.sub(r'\A#', r'##', line))
			f.write('\n')
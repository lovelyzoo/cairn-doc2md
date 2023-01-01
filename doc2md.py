import argparse
from markdownify import markdownify as md
from bs4 import BeautifulSoup
import re

preamble = '''---
layout: default
parent: Conversions
grand_parent: Adventures
title: {}
---
'''

if __name__ == "__main__":

	parser = argparse.ArgumentParser(
                    prog = 'doc2md',
                    description = 'Converts a google doc, exported as an html file, to markdown')
	
	parser.add_argument('infile')
	parser.add_argument('outfile')
	
	args = parser.parse_args()
	
	# Read the html file into bs4 object
	with open(args.infile, 'r') as f:
		soup = BeautifulSoup(f.read(), 'html.parser')

	# remove the style element
	soup.find('style').clear()
	
	# title is contained within the first p element
	title = soup.find('p').text
	preamble = preamble.format(title)
	  
	# convert html to markdown
	as_md = md(str(soup), heading_style="SETEXT", strip=['hr'], bullets = '-')
	
	with open(args.outfile, 'w') as f:
		f.write(preamble)
		f.write('\n'*3)

		# Make the title a markdown top level heading
		f.write('# ')

		for line in as_md.splitlines():
			# regex following deepens the level of all headings within the document
			f.write(re.sub(r'\A#', r'##', line))
			f.write('\n')
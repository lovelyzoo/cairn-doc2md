from markdownify import markdownify as md
from bs4 import BeautifulSoup
import re

# Read the html file into bs4 object
with open('TUDEBconversion.html', 'r') as f:
	soup = BeautifulSoup(f.read(), 'html.parser')
	
# remove the style element
soup.find('style').clear()
  
# convert html to markdown
as_md = md(str(soup), heading_style="SETEXT", strip=['hr'], bullets = '-')

preamble = '''---
layout: default
parent: Conversions
grand_parent: Adventures
title: Through Ultan's Door One
---


# '''

with open('TUD_one.md', 'w') as f:
	f.write(preamble)

	for line in as_md.splitlines():
		f.write(re.sub(r'\A#', r'##', line))
		f.write('\n')


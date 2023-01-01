
# cairn-doc2md

A python script that will convert a Google doc downloaded as an html file into a markdown script.
Developed to prepare documents for release to cairnrpg.com but likely has utility beyond that.

# Usage

Save your document using File->Download->'Web page' within the Google Docs UI. Extract the html file from the downloaded zip file.

Now type:
```
python3 cairn-doc2md.py path/to/htmlfile
```
and the document will be converted to markdown format and dumped to a file in the same directory as the cairn-doc2md script. The name of this file will be slugified from the title of the document.

Alternatively, if you want to specify the output file, do this:
```
python3 cairn-doc2md.py path/to/htmlfile path/to/outfile
```
 
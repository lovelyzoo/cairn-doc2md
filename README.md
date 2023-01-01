
# cairn-doc2md

A python script that will convert a Google doc downloaded as an html file into a markdown script.
Developed to prepare documents for release to cairnrpg.com but likely has utility beyond that.

# Usage

Save your document using File->Download->'Web page' within the Google Docs UI. Extract the html file from the downloaded zip file.

The command:
```
python3 cairn-doc2md.py path/to/htmlfile
```
will convert the document to markdown format and dump it to a file in the same directory as `cairn-doc2md.py`. The name of this file will be a slugified version of the document title.

Alternatively, if you want to specify the output file, do this:
```
python3 cairn-doc2md.py path/to/htmlfile path/to/outfile
```

# Worked example

The file `data/CairnAdventureConversionTemplate.html` has been downloaded from [this Google doc](https://docs.google.com/document/d/1-rfGGLmSc-SC5CL_8QXU5OSbNSyXF4yEfXDKwZrab2M/edit?usp=sharing).

Now run 
```
python3 cairn-doc2md.py data/CairnAdventureConversionTemplate.html
```
within the directory that this README is located and a file named `adventure-title.md` will be created.

View this file with the commandline:
```
cat adventure-title.md | less 
```
and you will notice that it is very similar to the [submission template](https://cairnrpg.com/submissions/adventure-conversions/#submission-template) on the Cairn website.
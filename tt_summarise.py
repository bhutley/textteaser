#!/usr/bin/python
import sys
import os
from textteaser import TextTeaser

if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
    print("Usage: %s <filename.txt>" % (sys.argv[0], ))
    print(" The first non-blank line of the file will be taken as the title")
    exit(0)

title = None
text = []

filename = sys.argv[1]
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if title is None:
            # We haven't got a title yet...
            
            if len(line) > 2:
                title = line
        else:
            text.append(line)

if title is None or len(text) == 0:
    print("No text to do summary with...")
    exit(0)

tt = TextTeaser()

sentences = tt.summarize(title, "\n".join(text))

for sentence in sentences:
  print sentence


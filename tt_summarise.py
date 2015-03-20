#!/usr/bin/python
import sys
import os
from textteaser import TextTeaser
import argparse

parser = argparse.ArgumentParser(description='Summarise a text file.')
parser.add_argument('-c', dest='sentence_count', type=int, nargs='?', default=5,
                   help='The number of sentences to summarise to')
parser.add_argument('filename', 
                   help='The file to process. The first non-blank line is interpreted as the title.')

args = vars(parser.parse_args())

sentence_count = args['sentence_count']
filename = args['filename']

if not os.path.isfile(filename):
    parser.print_help()
    exit(1)
    
title = None
text = []

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

sentences = tt.summarize(title, "\n".join(text), count=sentence_count)

for sentence in sentences:
  print sentence


#!/usr/bin/python
#!/usr/bin/env python

import csv
import getpass
import sys
import re
import traceback
import subprocess
import logging

wordlist = []

def generate_cloze(cloze,tl,nl,snd):
    tab = "\t"
    newline = "\n"    
    clz_prepend = "{{c1::"
    clz_postpend = "}}"
    replacement = clz_prepend + cloze + clz_postpend
    new_row_0 = tl.replace(cloze,replacement)
    cloze_line = new_row_0 + tab + nl + tab + snd
    return cloze_line

def main():

    with open("wordlist.csv") as f:
        reader = csv.reader(f, dialect='excel', delimiter='\t')
        for row in reader:
            wordlist.append(row[0])

    with open("consolidated.csv") as f:
        reader = csv.reader(f, dialect='excel', delimiter='\t')
        for row in reader:
            for element in wordlist:
                if element in row[0]:
                    print ( generate_cloze(element, row[0], row[1], row[2]) )

if __name__ == '__main__':
    try:
        exit_code = main()
    except Exception:
        traceback.print_exc()
        logging.error("Exception occurred", exc_info=True)
        exit_code = 1
    sys.exit(exit_code)

#!/usr/bin/env python
""""""

import re

def replacePattern(findresult):
    change = input("Enter an %s:\n" % findresult.group())
    return change

def madlid():
    madInFile = open("input.txt")
    madOutFile = open("output.txt", "w")
    madPattern = r"(ADJECTIVE|NOUN|ADVERB|VERB)"
    madMatch = re.compile(madPattern)
    resultMad = ""
    for line in madInFile:
        resultMad += madMatch.sub(replacePattern, line)
    madOutFile.write(resultMad)
    print("\n" + resultMad)

if __name__ == "__main__":
    madlid()
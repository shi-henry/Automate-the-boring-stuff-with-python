#!/usr/bin/env python

import re, shutil, os

def replaceMatch(matcher):
    print(matcher.group(0))
    Month = matcher.group(2)
    Day = matcher.group(3)
    Year = matcher.group(4)
    header = matcher.group(1)
    rear = matcher.group(6)
    print("hear is : '%s'" % header)
    fileName = header + Day + "-" + Month + "-" + Year + rear
    return fileName

os.chdir(r"c:\\")
fileNamePattern = r"""^(.*?)([0-1]?[0-9])-
                     ([0-3]?[0-9])-
                     ((19|20)\d\d)(.*?)$"""
fileNameRe = re.compile(fileNamePattern, re.VERBOSE)
for fileName in os.listdir("."):
    newFileName = fileNameRe.sub(replaceMatch, fileName)
    if newFileName != fileName:
        print(newFileName)
        shutil.copy(fileName, newFileName)
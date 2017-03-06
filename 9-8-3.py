#!/usr/bin/env python
""""""

import os, shutil, random, re

def gengrateFiles(inputPath, keyName):
    pathName = os.path.abspath(inputPath)
    if not os.path.isdir(pathName):
        os.makedirs(pathName)
    numList = [i for i in range(20)]
    numList = random.sample(numList, 10)
    print(numList)
    for num in numList:
        baseName = "%s%03d.txt" % (keyName, num)
        print(baseName)
        newFileName = os.path.join(pathName, baseName)
        newfile = open(newFileName, "w")
        newfile.write("%04d" % num)
        newfile.close()

def deleteSpace(inputPath, keyname):
    fileNamePattern = r"^%s\d{3}.txt$" % keyname
    fileNameRe = re.compile(fileNamePattern)
    absPathName = os.path.abspath(inputPath)
    nameList = os.listdir(absPathName)
    nameList.sort()
    print(nameList)
    startNum = 0;
    for fileName in nameList:
        if fileNameRe.match(fileName):
            targetName = "%s%03d.txt" % (keyname, startNum)
            sourceFileName = os.path.join(absPathName, fileName)
            targetFileName = os.path.join(absPathName, targetName)
            print(targetFileName)
            shutil.move(sourceFileName, targetFileName)
            startNum += 1;

# gengrateFiles(r"c:\\hehe", "spm")
deleteSpace(r"c:\\hehe", "spm")
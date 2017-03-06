#!/usr/bin/env python
""""""
import os, zipfile, datetime

def backupToZip(pathName):
    # os.chdir(r"C:\\")
    zipName = os.path.abspath(pathName)
    zipName = os.path.basename(zipName)
    currentTime = datetime.datetime.now()
    currentTime = currentTime.strftime("%Y-%m-%d-%H-%M-%S")
    zipName += "(" + currentTime + ")" + ".zip"
    print(zipName)
    backupZip = zipfile.ZipFile(zipName, "w")
    for folderName, subFolders, fileNames in os.walk(pathName):
        # folderName = os.path.abspath(folderName)
        backupZip.write(folderName)
        for fileName in fileNames:
            if fileName.startswith(os.path.basename(os.path.abspath(pathName)) + "(") and fileName.endswith(").zip"):
                continue
            backupZip.write(os.path.join(folderName, fileName))
    backupZip.close()
    print("Done")

backupToZip(".")
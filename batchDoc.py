import sys
import os

arguments = (sys.argv)
packageFolder = arguments[1]

fileList = os.listdir(packageFolder)
for file in fileList:
        file = packageFolder + "\\" + file
        print(file)
        os.system("start python.exe docMaster.py \"" + file + "\"")
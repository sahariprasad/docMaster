import sys
import os

arguments = (sys.argv)
packageFolder = arguments[1]
index = 1
fileList = os.listdir(packageFolder)
for file in fileList:
        file = packageFolder + "\\" + file
        print(str(index) + ". " + file)
        os.system("start python.exe docPrinter.py \"" + file + "\"")
        index += 1

os.system("start explorer.exe " + packageFolder)
print("Done.")
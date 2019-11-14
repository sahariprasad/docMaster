import xlsxwriter
import os

import zipfile
import re
lumxLocation = 'C:\\Users\hariprasads\\Downloads\\Channel.lumx' #You lumx file location here
packageLocation = (lumxLocation.split(".")[0])
outputXLSX = packageLocation + "\\Details.xlsx"
print(outputXLSX);
workbook = xlsxwriter.Workbook(outputXLSX)
dataSourceWS = workbook.add_worksheet('Data Sources')

with zipfile.ZipFile(lumxLocation, 'r') as zip_ref:
    zip_ref.extractall(packageLocation)

defaultApp = ""
headerFileLocation = packageLocation + "\\header.xml"
headerFile = open(headerFileLocation)

for line in headerFile:
    if re.search('<hi:property name="default_app">', line):
        defaultApp = line.split('default_app">')[1].split("<")[0]

fileLocation = packageLocation + "\\apps\\" + defaultApp + "\\content.biapp"

componentName = ""
dataSource = ""

dataSourceArray = []
componentArray = []
globalVariableArray = []

datasourceAlias = ""
datasourceName = ""

row = 0
col = 0

sourceFile = open(fileLocation, encoding="utf8")
print("Data Sources: ")
for line in sourceFile:
    if re.search('bi:data_source_alias name=', line):
        ds_alias = line.split("name=\"")[1].split("\"")[0]
        dataSourceArray.append(ds_alias)
        dataSourceWS.write(row, col, ds_alias)
    if re.search('bi:property name="DATA_SOURCE_NAME"', line):
        ds_name = line.split("value=\"")[1].split("\"")[0]
        dataSourceArray.append(ds_name)
        dataSourceWS.write(row, col+1, ds_name)
        row = row + 1

for x in dataSourceArray:
    print(x)

componentWS = workbook.add_worksheet('Components')
row = 0
col = 0
sourceFile = open(fileLocation, encoding="utf8")
print("\nComponents with data source mappings:")
for line2 in sourceFile:

    if re.search('<bi:component name=', line2):
        componentName = line2.split("name=\"")[1].split("\"")[0]
    if re.search('<bi:property name="DATA_SOURCE_ALIAS_REF"', line2):
        dataSource = line2.split("value=\"")[1].split("\"")[0]
        if (dataSource != ""):
            componentArray.append(componentName + " - " + dataSource)
            componentWS.write(row, col, componentName)
            componentWS.write(row, col + 1, dataSource)
            row = row + 1

for x in componentArray:
    print(x)

globalVariableWS = workbook.add_worksheet('Global Variables')
row = 0
col = 0
sourceFile = open(fileLocation, encoding="utf8")
print("\nGlobal Variables:")
for line in sourceFile:
    if re.search('bi:property name="GLOBALVARIABLE"', line):
        globalVarName = (next(sourceFile)).split("value=\"")[1].split("\"")[0]
        globalVariableArray.append(globalVarName)
        globalVariableWS.write(row, col, globalVarName)
        row = row + 1


for x in globalVariableArray:
    print(x)

workbook.close()
os.system("start EXCEL.EXE " + outputXLSX)
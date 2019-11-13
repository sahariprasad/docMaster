import xlsxwriter
import os

import zipfile
import re
lumxLocation = 'C:\\Users\hariprasads\\Downloads\\Channel.lumx' #You lumx file location here
packageLocation = (lumxLocation.split(".")[0])
outputXLSX = packageLocation + "\\Details.xlsx"

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

dataSourceWS.write(0,0, 'Data Source Alias')
dataSourceWS.write(0,1, 'Data Source Type')
dataSourceWS.write(0,2, 'Data Source Name')
row = 1
col = 0

sourceFile = open(fileLocation, encoding="utf8")

for line in sourceFile:
    if re.search('bi:data_source_alias name=', line):
        ds_alias = line.split("name=\"")[1].split("\"")[0]
        dataSourceArray.append(ds_alias)
        dataSourceWS.write(row, col, ds_alias)

    if re.search('bi:property name="DATA_SOURCE_TYPE"', line):
        ds_name = line.split("value=\"")[1].split("\"")[0]
        dataSourceArray.append(ds_name)
        dataSourceWS.write(row, col+1, ds_name)

    if re.search('bi:property name="DATA_SOURCE_NAME"', line):
        ds_name = line.split("value=\"")[1].split("\"")[0]
        dataSourceArray.append(ds_name)
        dataSourceWS.write(row, col+2, ds_name)
        row = row + 1

componentWS = workbook.add_worksheet('Components')

componentWS.write(0,0, 'Component Name')
componentWS.write(0,0, 'Component Data Source')
row = 1
col = 0
sourceFile = open(fileLocation, encoding="utf8")

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

globalVariableWS = workbook.add_worksheet('Global Variables')

globalVariableWS.write(0,0, 'Global Variable')
row = 1
col = 0
sourceFile = open(fileLocation, encoding="utf8")

for line in sourceFile:
    if re.search('bi:property name="GLOBALVARIABLE"', line):
        globalVarName = (next(sourceFile)).split("value=\"")[1].split("\"")[0]
        globalVariableArray.append(globalVarName)
        globalVariableWS.write(row, col, globalVarName)
        row = row + 1

workbook.close()
os.system("start EXCEL.EXE " + outputXLSX)
print ("Opening " + outputXLSX)
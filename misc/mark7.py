import re

fileLocation = "C:\\Users\\hariprasads\\OneDrive - Visual Bi Solutions Inc\\Desktop\\content2.xml" #replace this with your .biapp file

componentName = ""
dataSource = ""

dataSourceArray = []
componentArray = []
globalVariableArray = []

datasourceAlias = ""
datasourceName = ""

sourceFile = open(fileLocation)
print("Data Sources: ")
for line in sourceFile:
    if re.search('bi:data_source_alias name=', line):
        dataSourceArray.append(line.split("name=\"")[1].split("\"")[0])
    if re.search('bi:property name="DATA_SOURCE_NAME"', line):
        dataSourceArray.append(line.split("value=\"")[1].split("\"")[0])

    # dataSourceArray.append(datasourceAlias + " - " + datasourceName)

for x in dataSourceArray:
    print(x)

sourceFile = open(fileLocation)
print("\nComponents with data source mappings:")
for line2 in sourceFile:

    if re.search('<bi:component name=', line2):
        componentName = line2.split("name=\"")[1].split("\"")[0]
    if re.search('<bi:property name="DATA_SOURCE_ALIAS_REF"', line2):
        dataSource = line2.split("value=\"")[1].split("\"")[0]
        if (dataSource != ""):
            componentArray.append(componentName + " - " + dataSource)

for x in componentArray:
    print(x)

sourceFile = open(fileLocation)
print("\nGlobal Variables:")
for line in sourceFile:
    if re.search('bi:property name="GLOBALVARIABLE"', line):
        globalVariableArray.append((next(sourceFile)).split("value=\"")[1].split("\"")[0])


for x in globalVariableArray:
    print(x)
import re
defaultApp = ""

packageLocation = "C:\\Users\hariprasads\\Downloads\\Channel"

headerFileLocation = packageLocation + "\\header.xml"
headerFile = open(headerFileLocation)

for line in headerFile:
    if re.search('<hi:property name="default_app">', line):
        defaultApp = line.split('default_app">')[1].split("<")[0]


fileLocation = packageLocation + "\\apps\\" + defaultApp + "\\content.biapp"
print(fileLocation)


componentName = ""
dataSource = ""

dataSourceArray = []
componentArray = []
globalVariableArray = []

datasourceAlias = ""
datasourceName = ""

sourceFile = open(fileLocation, encoding="utf8")
print("Data Sources: ")
for line in sourceFile:
    if re.search('bi:data_source_alias name=', line):
        dataSourceArray.append(line.split("name=\"")[1].split("\"")[0])
    if re.search('bi:property name="DATA_SOURCE_NAME"', line):
        dataSourceArray.append(line.split("value=\"")[1].split("\"")[0])

    # dataSourceArray.append(datasourceAlias + " - " + datasourceName)

for x in dataSourceArray:
    print(x)

sourceFile = open(fileLocation, encoding="utf8")
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

sourceFile = open(fileLocation, encoding="utf8")
print("\nGlobal Variables:")
for line in sourceFile:
    if re.search('bi:property name="GLOBALVARIABLE"', line):
        globalVariableArray.append((next(sourceFile)).split("value=\"")[1].split("\"")[0])


for x in globalVariableArray:
    print(x)
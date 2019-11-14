import xml.dom.minidom
from xml.dom.minidom import Node

doc = xml.dom.minidom.parse("C:\\Users\\hariprasads\\OneDrive - Visual Bi Solutions Inc\\Desktop\\content2.xml");
print (doc.nodeName)
print (doc.firstChild.tagName)
# print(doc.__getattribute__())
# print(doc.firstChild.firstChild.tagName)
componentList = doc.getElementsByTagName("bi:data_source_alias")
for component in componentList:
    print(component.getAttribute)

# doc.
# ROOT = doc.getElementsByTagName('ROOT')

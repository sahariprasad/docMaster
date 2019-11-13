import xml.etree.ElementTree as ET
tree = ET.parse('C:\\Users\\hariprasads\\OneDrive - Visual Bi Solutions Inc\\Desktop\\content.xml')
root = tree.getroot()

# print(root.tag)
# print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

# for ROOT in root.findall('ABSOLUTE_LAYOUT_COMPONENT'):
#     name = ROOT.get('name')
#     print(name)
#


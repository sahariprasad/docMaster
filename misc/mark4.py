from xml.etree import ElementTree as et
s = '<bi:data_source_alias name="DS_4" type="QUERY_DATA_SOURCE">'
tree = et.fromstring(s)
print(tree.find('name'))

from bs4 import BeautifulSoup
import lxml

xml_file = "C:\\Users\\hariprasads\\OneDrive - Visual Bi Solutions Inc\\Desktop\\content2.xml"

with open(xml_file, "r", encoding="utf8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "lxml")

    items = soup.find_all("bi:data_source_alias")
    # # print(soup.get_text)
    # for item in items:
    #     print(soup.getText)
    print (items)

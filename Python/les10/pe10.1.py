#1723682
#David van Vliet

import xmltodict

xml =open("artikelen.xml")
xml_data = xml.read()
data = xmltodict.parse(xml_data)
#print(data)
for item in data["artikelen"]["artikel"]:
    print(item["naam"])
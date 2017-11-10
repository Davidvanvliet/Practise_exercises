#1723682
#David van Vliet

import xmltodict

xml =open("artikelen.xml")
xml_data = xml.read()
data = xmltodict.parse(xml_data)

#zoekt in het xml bestand op het niveau van artikel voor alle namen en print deze
for item in data["artikelen"]["artikel"]:
    print(item["naam"])
import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

boeken = processXML('boeken.xml')
bookdict = boeken ['catalog']['book']
for book in bookdict:
    author = book['author']
    title = book['title']
    price = book['price']
    print(author, title, price)

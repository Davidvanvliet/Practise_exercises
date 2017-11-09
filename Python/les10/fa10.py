#1723682
#David van Vliet

import xmltodict
# Het xml bestand openen en lezen
def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

a = processXML('FA10.xml')
b = a ['Stations']['Station']
#in het xml bestand navigeren naar de betreffende regels voor de code en het type en deze printen
print('Dit zijn de codes en types van de 4 stations:')
for station in b:
    code = station['Code']
    type = station['Type']
    print (code, '-', type)

print()
#Als synoniemen niet leeg is, dan deze betreffende code printen
print('Dit zijn de stations met één of meer synoniemen')
for station in b:
    if station ['Synoniemen'] is not None:
        synoniem = station['Synoniemen']
        code = station['Code']
        print(code, '-', synoniem)

print()
#in het xml bestand navigeren naar de betreffende regels voor de code en het type en deze printen
print('Dit is de lange naam van elk station:')
for station in b:
    code = station['Code']
    lang = station['Namen']['Lang']
    print (code, '-', lang)

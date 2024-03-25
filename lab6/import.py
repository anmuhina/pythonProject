from xml.dom import minidom

xmldoc = minidom.parse('paintingsForRead.xml')
paintingsList = xmldoc.getElementsByTagName('painting')

id = []
title = []
year = []
genre = []
artistName = []
artistBirthYear = []

for painting in paintingsList:
    id.append(painting.getElementsByTagName('id')[0].firstChild.nodeValue)
    title.append(painting.getElementsByTagName('title')[0].firstChild.nodeValue)
    year.append(painting.getElementsByTagName('year')[0].firstChild.nodeValue)
    genre.append(painting.getElementsByTagName('genre')[0].firstChild.nodeValue)
    artist = painting.getElementsByTagName('artist')[0]
    artistName.append(artist.getElementsByTagName('name')[0].firstChild.nodeValue)
    artistBirthYear.append(artist.getElementsByTagName('birthYear')[0].firstChild.nodeValue)

for i in range(0, len(paintingsList)):
    print(f"Картина №{id[i]}:\n название:'{title[i]}';\n год написания:{year[i]};\n художник:{artistName[i]} "
          f"({artistBirthYear[i]});\n направление живописи:{genre[i]}\n\n")

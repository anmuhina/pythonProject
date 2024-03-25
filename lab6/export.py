from xml.dom import minidom

xmldoc = minidom.parse('paintingsForWrite.xml')

rootNode = xmldoc.documentElement

# Картина 1
paintingNode1 = xmldoc.createElement("painting")

idNode1 = xmldoc.createElement("id")
idNode1.appendChild(xmldoc.createTextNode("1"))
paintingNode1.appendChild(idNode1)

titleNode1 = xmldoc.createElement("title")
titleNode1.appendChild(xmldoc.createTextNode("The Starry Night"))
paintingNode1.appendChild(titleNode1)

artistNode1 = xmldoc.createElement("artist")
artistNode1.appendChild(xmldoc.createTextNode("Vincent Van Gogh"))
paintingNode1.appendChild(artistNode1)

yearNode1 = xmldoc.createElement("year")
yearNode1.appendChild(xmldoc.createTextNode("1889"))
paintingNode1.appendChild(yearNode1)

genreNode1 = xmldoc.createElement("genre")
genreNode1.appendChild(xmldoc.createTextNode("Landscape"))
paintingNode1.appendChild(genreNode1)

rootNode.appendChild(paintingNode1)


# Картина 2
paintingNode2 = xmldoc.createElement("painting")

idNode2 = xmldoc.createElement("id")
idNode2.appendChild(xmldoc.createTextNode("2"))
paintingNode2.appendChild(idNode2)

titleNode2 = xmldoc.createElement("title")
titleNode2.appendChild(xmldoc.createTextNode("Mona Lisa"))
paintingNode2.appendChild(titleNode2)

artistNode2 = xmldoc.createElement("artist")
artistNode2.appendChild(xmldoc.createTextNode("Leonardo Da Vinci"))
paintingNode2.appendChild(artistNode2)

yearNode2 = xmldoc.createElement("year")
yearNode2.appendChild(xmldoc.createTextNode("1506"))
paintingNode2.appendChild(yearNode2)

genreNode2 = xmldoc.createElement("genre")
genreNode2.appendChild(xmldoc.createTextNode("Portrait"))
paintingNode2.appendChild(genreNode2)

rootNode.appendChild(paintingNode2)


with open('paintingsForWrite.xml', 'w') as f:
		xmldoc.writexml(f, addindent='  ', newl='\n', encoding='utf-8')

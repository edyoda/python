import xml.etree.ElementTree as ET
tree = ET.parse('movies.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

for movie in root.iter('movie'):
    print(movie.attrib)


for description in root.iter('description'):
    print(description.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
    print(movie.attrib)

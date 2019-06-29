import xml.etree.ElementTree as xml

def updateXML(filename):
    # Start with the root element
    tree = xml.ElementTree(file=filename)
    root = tree.getroot()

    for salary in root.iter("salary"):
        salary.text = '1000'
 
    tree = xml.ElementTree(root)
    with open("updated_test.xml", "wb") as fh:
        tree.write(fh)

if __name__ == "__main__":
    updateXML("student.xml")

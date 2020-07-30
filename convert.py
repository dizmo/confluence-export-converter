import xml.etree.ElementTree as ET

# entities.xml is contained in xmlexport-[date & time].zip
tree = ET.parse('entities.xml')
root = tree.getroot()

users = {}
toRemove = []

for child in root:
    if child.attrib["class"] == "ConfluenceUserImpl":
        id = list(child)[0].text
        user = list(child)[1].text
        
        # set lowerName tag's text to name tag's text (made lowercase) per default
        list(child)[2].text = user.lower()
                
        # record duplicate users and replace user IDs with the first found user's
        if user in users:
            # recursively iterate through all children objects
            for elem in root.iter():
                if elem.text is not None:
                    elem.text = elem.text.replace(id, users[user])
            toRemove.append(child)
        else:
            # record ID upon user's first occurrence
            users[user] = id

for child in toRemove:
    root.remove(child)

tree.write('entities_converted.xml')


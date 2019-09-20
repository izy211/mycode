#!/usr/bin/env python3
import re
import xml.etree.ElementTree as ET
tree = ET.parse("moviesdat.xml")
root = tree.getroot()
for movie in root.iter("moviesdat.xml"):
    print(movie.attrib)

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
print(b2tf)
b2tf.attrib["title"] = "Back to the Future"
print(b2tf.attrib)

for form in root.findall("./genre/decade/movie/format"):
    print(form.attrib, form.text)
    match = re.search(",", form.text)
    if match:
        form.set("multiple","Yes")
    else:
        form.set("multiple","No")

for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, "\n")

for movie in root.findall("./genre/decade/movie/[year='2000']"):
    print(movie.attrib)


action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, "decade")
new_dec.attrib["years"] = "2000s"

xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000 = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000.append(xmen)
dec1990 = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1980 = root.find("./genre[@category='Thriller']/decade[@years='1980s']")
dec1990.remove(xmen)

ampsy = root.find("./genre/decade/movie[@title='American Psycho']")
dec2000.append(ampsy)
dec1980.remove(ampsy)

tree.write("moviesdatUPDATED.xml")
tree = ET.parse("moviesdatUPDATED.xml")
root = tree.getroot()

for movie in root.iter("movie"):
    print(movie.attrib)
for decade in root.findall("./genre/decade"):
    print(decade.attrib)
    for year in decade.findall("./movie/year"):
        print(year.text, "\n")

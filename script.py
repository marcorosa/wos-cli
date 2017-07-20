import xml.etree.ElementTree as ET
import re

from config import user_id, password
from tabulate import tabulate
from wos import WosClient


client = WosClient(user_id, password)
client.connect()

sp5 = client.search('AU=Surname Name',
                    count=100,
                    offset=1,
                    timeSpan={'begin': '2012-01-01',
                              'end': '2018-01-01'})

# Format xml
my_xml = re.sub(' xmlns="[^"]+"', '', sp5.records, count=1).encode('utf-8')
tree = ET.fromstring(my_xml)

# Get results
res = []
for t in tree:
    element = list(t)
    idwos = element[0].text
    data = list(element[1])    # static_data
    summary = list(data[0])    # summary
    titles = list(summary[2])  # titles
    year = summary[1].attrib['pubyear']
    paper = ''
    for title in titles:
        if title.attrib['type'] == 'item':
            paper = title.text
    res.append([year, paper, idwos])

print tabulate(res,
               headers=['year', 'id', 'title'],
               tablefmt='fancy_grid',
               missingval='?')

import re
import suds
import texttable as tt
import xml.etree.ElementTree as ET

from config import user_id, password
from datetime import date
from six import print_
from wos import WosClient


def _draw_table(data):
    # Generate table
    tab = tt.Texttable()
    tab.add_rows(data)
    tab.set_cols_align(['l', 'l', 'l'])
    tab.header(['Year', 'Title', 'ID WOS'])
    tab.set_cols_width([5, 55, 20])  # Use fixed terminal dimension (80 char)
    s = tab.draw()
    print_(s)


def search(author, years, results, affiliation=None):
    try:
        client = WosClient(user_id, password)
        client.connect()
    except suds.WebFault:
        print_('Username and/or password not valid')
        exit(1)

    # Build query
    if affiliation:
        query = 'AU=%s AND AD=%s' % (author, affiliation)
    else:
        query = 'AU=%s' % author

    # Build timespan
    current_year = date.today().year

    sq = client.search(query,
                       count=results,
                       offset=1,
                       timeSpan={'begin': '%s-01-01' % (current_year - years),
                                 'end': '%s-01-01' % (current_year + 1)})

    # Format xml
    my_xml = re.sub(' xmlns="[^"]+"', '', sq.records, count=1).encode('utf-8')
    tree = ET.fromstring(my_xml)

    n = len(list(tree))
    if n > 0:
        print_('Found %s papers' % n)
    else:
        print_('No papers found for %s in the last %s years' % (author, years))
        exit(0)

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
    res.sort(key=lambda x: x[0], reverse=True)
    _draw_table(res)

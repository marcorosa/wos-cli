import re
import suds
import texttable as tt
import xml.etree.ElementTree as ET

from .config import user_id, password
from datetime import date
from operator import itemgetter
from six import print_
from wos import WosClient


def _draw_table(data):
    # Generate table
    tab = tt.Texttable()
    tab.set_cols_align(['l', 'l', 'l'])
    tab.add_rows(data, header=False)
    tab.header(['Year', 'Title', 'ID WOS'])
    tab.set_cols_width([5, 55, 20])  # Use fixed terminal dimension (80 char)
    s = tab.draw()
    print_(s)


def query(client, author, years, results, affiliation=None):
    # Build query
    if affiliation:
        query = 'AU=%s AND AD=%s' % (author, affiliation)
    else:
        query = 'AU=%s' % author

    # Build timespan
    current_year = date.today().year
    date_start = '{}-01-01'.format(current_year - years)
    date_stop = '{}-01-01'.format(current_year + 1)

    sq = client.search(query,
                       count=results,
                       offset=1,
                       timeSpan={'begin': date_start, 'end': date_stop})

    # Format xml
    my_xml = re.sub(' xmlns="[^"]+"', '', sq.records, count=1).encode('utf-8')
    tree = ET.fromstring(my_xml)

    n = len(list(tree))
    if n > 0:
        print_('Found %s papers' % n)
    else:
        print_('No papers found for %s in the last %s years' % (author, years))
        exit(0)
    return tree


def tree_extractor(tree):
    # Get results
    results = []
    for t in tree:
        idwos = t.find('UID').text
        year = t.find('.//pub_info').attrib.get('pubyear', '?')
        paper = t.find('.//title[@type="item"]').text
        results.append([year, paper, idwos])
    results = sorted(results, key=itemgetter(0), reverse=True)
    return results


def search(author, years, results, affiliation=None):
    try:
        client = WosClient(user_id, password)
        client.connect()
    except suds.WebFault as e:
        print_('Username and/or password not valid, or requests limit exceeded')
        print_(e)
        exit(1)

    # Build the tree
    tree = query(client, author, years, results, affiliation)
    # Extract information from the tree
    results = tree_extractor(tree)
    # Draw the table
    _draw_table(results)
    return results

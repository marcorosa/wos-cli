import csv
import sqlite3
import suds

from .config import user_id, password
from .dbconn import _init_db
from .search import query, tree_extractor
from six import print_
from wos import WosClient


def _extract_and_write(tree, author, outfile):
    results = tree_extractor(tree)
    # Write results in db
    with sqlite3.connect(outfile) as connection:
        connection.executemany('INSERT OR IGNORE INTO authors VALUES (?,?,?,?)',
                               (((author, entry[0], entry[1], entry[2]))
                                for entry in results))


def multiple_search(infile, outfile, years=5, results=100):
    try:
        client = WosClient(user_id, password)
        client.connect()
    except suds.WebFault as e:
        print_('Username and/or password not valid, or requests limit exceeded')
        print_(e)
        exit(1)

    # Initialize db and table (if not existing)
    _init_db(outfile)

    with open(infile) as f:
        reader = csv.DictReader(f)
        for r in reader:
            # Search papers for this author
            print_('Searching author %s' % r.get('author'))
            tree = query(client, r.get('author').strip(), years, results,
                         r.get('affiliation').strip())
            _extract_and_write(tree, r.get('author'), outfile)

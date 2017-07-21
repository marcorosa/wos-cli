import os
import sqlite3

from six import print_


DBFILE = 'data/authors.db'


def _init_db(dbfile):
    if os.path.isfile(dbfile):
        print_('Database file already exists. Data will be appended')
        return
    with sqlite3.connect(dbfile) as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS'
                           ' authors(author, year, entry, wos_id UNIQUE)')
    print_('Db created!')


def _filter_records(author, records):
    with sqlite3.connect(DBFILE) as connection:
        c = connection.cursor()
        c.execute('SELECT * FROM authors WHERE author = ?', (author,))
        all_rec = c.fetchall()
    all_ids = map(lambda x: x[3], all_rec)
    records = list(filter(lambda x: x[2] not in all_ids, records))
    print_('Found %s new records' % len(records))
    return records


def save(author, data):
    _init_db(DBFILE)

    # Filter already existing entries
    data = _filter_records(author, data)
    if len(data) < 1:
        print_('No records to add')
        exit(0)

    with sqlite3.connect(DBFILE) as connection:
        connection.executemany('INSERT OR IGNORE INTO authors VALUES (?,?,?,?)',
                               (((author, row[0], row[1], row[2]))
                                for row in data))

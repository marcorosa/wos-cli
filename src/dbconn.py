import os
import sqlite3

from six import print_


DBFILE = 'author_wos.db'


def init_db(dbfile):
    if os.path.isfile(dbfile):
        print_('Database file already exists. Data will be appended')
        return
    with sqlite3.connect(dbfile) as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS'
                           ' authors(author, year, entry, wos_id UNIQUE)')
    print_('Db created!')


def save(author, data):
    init_db(DBFILE)
    with sqlite3.connect(DBFILE) as connection:
        connection.executemany('INSERT OR IGNORE INTO authors VALUES (?,?,?,?)',
                               (((author, row[0], row[1], row[2]))
                                for row in data))

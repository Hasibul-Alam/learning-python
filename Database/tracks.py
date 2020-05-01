import xml.etree.ElementTress as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;
drop table if exists Genre;

create table Artist(
    id INTEGERE NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

create table Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTERGER,
    title TEXT UNIQUE
);

CREATE TABLE Table (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER, rationg INTEGER, count INTEGER
);
''')

fname = input('Enter the file name: ')
if len(fname) < 1 : fname = 'Library.xml'

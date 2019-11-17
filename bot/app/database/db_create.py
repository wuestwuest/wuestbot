#!/usr/bin/env python3

"""
This script sets up the database as needed for the project. It is not really a 
module of the bot since it is not imported somewhere but just resides here for
later reference and if the re-creation of the db should be necessary. 
For further understanding see corresponding UML diagram.
"""

""" to do:
- might check for long strings in descriptions etc
"""

import sqlite3
import logging
import os

logging.basicConfig(filename=os.path.abspath('../log.txt'), level=logging.DEBUG)

conn = sqlite3.connect('data.sqlite')
curs = conn.cursor()

curs.execute("""
    create table Users if not exists(
    uID integer primary key, 
    uName text,
    isBot bool)
    """)

curs.execute("""
    create table Events if not exists( 
    eventID integer primary key,
    eName text, 
    date text, 
    time text, 
    desc text, 
    admission text, 
    ePicID text,
    loca text)
    """)

curs.execute("""
    create table Artists if not exists(
    aName text primary key, 
    website text, 
    soundcloud text, 
    bandcamp text, 
    bio text, 
    aPicID text)
    """)

curs.execute("""
    create table PlaysAt if not exists(
    aName text, 
    eName text,
    date text, 
    foreign key (aName) references Artists (aName), 
    foreign key (eName, date) references Events (eName, date)
    )
    """)
#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('127.0.0.1', 'root', 'root', 'testdb', port=8889,);

with con:
    cur = con.cursor()
    print type(cur)
    cur.execute("SELECT * FROM Writers")
    a = cur.fetchall()
    print a

    desc = cur.description
    print desc

print "***********"

with con:

    cur1 = con.cursor(mdb.cursors.DictCursor)
    print type(cur1)
    cur1.execute("SELECT * FROM Writers")

    l = cur1.fetchone()
    print l

    rows = cur1.fetchall()
    print rows

    for row in rows:
        print row["Id"], row["Name"]

    '''
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")
    '''
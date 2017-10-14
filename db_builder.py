# Jake Zaia
# SoftDev p09
# 2017-10-13
# Work09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# Populates courses
c.execute("CREATE TABLE courses (code str, mark int, id int);")

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT INTO courses VALUES ("' + str(row['code']) + '",' + str(row['mark']) + ',' + str(row['id']) + ');')

# Populates peeps
c.execute("CREATE TABLE peeps (name str, age int, id int);")

with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT INTO peeps VALUES ("' + str(row['name']) + '",' + str(row['age']) + ',' + str(row['id']) + ');')


command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database



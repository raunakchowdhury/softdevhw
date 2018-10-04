#Raunak Chowdhuey
#SoftDev1 pd8
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
# courses.csv
with open('raw/courses.csv') as csvfile: #open csv file and store as DictReader
    reader = csv.DictReader(csvfile) #{header: element, header2, element2,..}
    command = 'CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)'
    c.execute(command)
    for lines in reader:
        #print(lines.keys())
        #print(lines)
        #print(lines.values())
        command = 'INSERT INTO courses VALUES(\"{}\",{},{})'.format(lines['code'], int(lines['id']), int(lines['mark']))
        #print(command)
        c.execute(command)

with open('raw/occupations.csv') as csvfile: #open csv file and store as DictReader
    reader = csv.DictReader(csvfile) #{header: element, header2, element2,..}
    command = 'CREATE TABLE occupations (Job Class TEXT, Percentage INTEGER)'
    c.execute(command)
    for lines in reader:
        cleaned_job = lines['Job Class'].strip('\"')
        command = 'INSERT INTO occupations VALUES(\"{}\",{})'.format(cleaned_job, float(lines['Percentage']))
        c.execute(command)

with open('raw/peeps.csv') as csvfile: #open csv file and store as DictReader
    reader = csv.DictReader(csvfile) #{header: element, header2, element2,..}
    command = 'CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)'
    c.execute(command)
    for lines in reader:
        command = 'INSERT INTO peeps VALUES(\"{}\",{},{})'.format(lines['name'], int(lines['age']), int(lines['id']))
        c.execute(command)
#==========================================================

db.commit() #save changes
db.close()  #close database

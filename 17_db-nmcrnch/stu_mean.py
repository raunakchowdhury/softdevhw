# Raunak Chowdhury
# Softdev1 pd8
# K#17: Average
#2018-10-05

import sqlite3

DB_FILE="discobandit.db"

def lookup_grades(student):
    '''
    Lists the grades for one student in all subjects.
    WARNING: Namespace conflicts will prevent this function from working properly
    '''
    return_string = 'Grades of {}:\n'.format(student) # will contain all the relevant info
    student = '\"{}\"'.format(student) # necessary for comparing names

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    command = 'SELECT code, mark FROM peeps, courses WHERE peeps.id = courses.id AND name = {}'.format(student) #find courses taken by that student
    c.execute(command)

    # each entry is organized as (code,mark)
    for entry in c:
        return_string += 'Course: {} Grade: {}\n'.format(entry[0], entry[1])

    db.close()
    return return_string

def compute_average(student):
    '''
    Computes the average for one student.
    WARNING: Namespace conflicts will prevent this function from working properly
    '''
    student = '\"{}\"'.format(student) # necessary for comparing names
    average = 0
    num_subjects = 0 # keeps track of the number of subjects taken

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    command = 'SELECT code, mark FROM peeps, courses WHERE peeps.id = courses.id AND name = {}'.format(student) #find courses taken by that student
    c.execute(command)

    # each entry is organized as (code,mark)
    for entry in c:
        average += entry[1]
        num_subjects += 1

    db.close()
    return average / num_subjects

def display_info():
    '''
    Extracts the name, average, and id of each user in the sqlite3 db and displays it.
    '''
    return_string = '' # will contain all the relevant info

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    # Grade lookup
    command = 'SELECT name, courses.mark, peeps.id FROM peeps, courses WHERE peeps.id = courses.id' #Match ids and then report the name of the courses taken
    c.execute(command)

    name_dict = {} # dict will store values as {'name': [grade, # courses taken, id]}
    #each row is (name, mark, id)
    for row in c:
        if row[0] not in name_dict:
            name_dict[row[0]] = [row[1], 1, row[2]]
        else:
            # increment the # courses taken by 1 and add the mark to the current grade total
            entry = name_dict[row[0]]
            entry[0] += row[1]
            entry[1] += 1

    # turn the num value of the dict into the average
    for key in name_dict.keys():
        info_list = name_dict[key] #list that contains [grade, # courses, id]
        info_list[0] = info_list[0] / info_list[1]
        return_string += 'Name: {} Average: {} ID: {}\n'.format(key, info_list[0], info_list[2])

    db.close()
    return return_string

def generate_average_table():
    '''
    Extracts the name, average, and id of each user in the sqlite3 db and generates a table that is then stored in the db.
    '''

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    # Grade lookup
    command = 'SELECT name, courses.mark, peeps.id FROM peeps, courses WHERE peeps.id = courses.id' #Match ids and then report the name of the courses taken
    c.execute(command)

    name_dict = {} # dict will store values as {'name': [grade, # courses taken, id]}

    #each row is (name, mark, id)
    for row in c:
        if row[0] not in name_dict:
            name_dict[row[0]] = [row[1], 1, row[2]]
        else:
            # increment the # courses taken by 1 and add the mark to the current grade total
            entry = name_dict[row[0]]
            entry[0] += row[1]
            entry[1] += 1

    # create the table or not depending on whether if its there or not
    command = 'CREATE TABLE peeps_avg(id INTEGER, average FLOAT) '
    c.execute(command)

    # turn the num value of the dict into the average
    for key in name_dict.keys():
        info_list = name_dict[key] #list that contains [grade, # courses, id]
        info_list[0] = info_list[0] / info_list[1]
        #insert the values in as (id, avg)
        command_tuple = (info_list[2], info_list[0])
        c.execute('INSERT INTO peeps_avg VALUES(?,?)', command_tuple)

    db.commit()
    db.close()

def add_course(code, new_id, mark):
    '''
    Adds a new row to the database with the parameters code, id, and mark.
    code --> string
    id --> integer
    mark --> integer
    '''
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    code = '\"{}\"'.format(code) # necessary for comparing names

    # find and update the peeps_avg table with the new value
    command_tuple = (code, new_id, mark)
    c.execute('INSERT INTO courses VALUES(?,?,?)', command_tuple)

    db.commit()
    db.close()

if __name__ == '__main__':
    generate_average_table()
    print(lookup_grades('kruder'))
    print('Average of kruder: {}'.format(compute_average('kruder')))
    add_course('apcs', 1, 95)
    print('Average of kruder after adding apcs: {}'.format(compute_average('kruder')))
    print(lookup_grades('kruder'))
    print('Printing info for all students:\n{}'.format(display_info()))

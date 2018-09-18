from flask import Flask

app = Flask(__name__) #create an instance of the Flask class

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/tbm')
def tbm():
    return 'Tofr says: Atom is the best religion'

@app.route('/sk')
def sk():
    return 'K says: Emacs is the best religion'

@app.route('/dw')
def dw():
    return 'DW says: vim is the best religion'

@app.route('/<every_other_student>')
def student(every_other_student):
    return '{} says: Atom is the best religion'.format(every_other_student)

app.debug = True
app.run()

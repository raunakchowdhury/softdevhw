# Raunak Chowdhury
# Softdev1 pd8
# K# ##:  text
#2018- ##- ##

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth', methods = ['POST', 'GET'])
def auth():
    if request.method == 'POST':
        return render_template('greeting.html', name = request.form['name'], method = request.method)
    return render_template('index.html', resubmit = True)

if __name__ == '__main__':
    print(app)
    app.debug = True
    app.run()

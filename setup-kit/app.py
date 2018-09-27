# Raunak Chowdhury
# Softdev1 pd8
# K# ##:  text
#2018- ##- ##

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()

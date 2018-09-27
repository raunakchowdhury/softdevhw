# Raunak Chowdhury
# Softdev1 pd8
# K#13: Echo Echo Echo
#2018-09-24

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth')#, methods = ['POST'])
def auth():
    print(app)
    print(request)
    name = request.args['name']
    method = request.method
    return render_template('greeting.html', name = name, method = method)

if __name__ == '__main__':
    print(app)
    app.debug = True
    app.run()

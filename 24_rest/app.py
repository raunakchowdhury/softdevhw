# Raunak Chowdhury
# Softdev1 pd8
# K#24: A RESTful Journey Skyward
#2018-13-11

from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

@app.route('/')
def home():
    response = request.urlopen('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=Q4shlQsSkS7N9DZP7zmquItAvooD3kG0C6SZqqwT')
    response = response.read()
    info = json.loads(response)
    return render_template('index.html', image=info['url'])

if __name__ == '__main__':
    app.debug=True
    app.run()

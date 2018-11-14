# Raunak Chowdhury
# Softdev1 pd8
# K#25: Getting More REST
#2018-14-11

from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

@app.route('/')
def home():
    API_KEY = 'bUgjCDGGBjoEt4usv0C7XVTorrT9jlg7'
    URL_STUB = 'http://api.giphy.com/v1/gifs/search?q=nyan_cat&api_key='
    URL = URL_STUB + API_KEY
    response = request.urlopen(URL)
    response = response.read()
    info = json.loads(response)
    return render_template('index.html', api=info['data'][0]['embed_url'])

if __name__ == '__main__':
    app.debug=True
    app.run()

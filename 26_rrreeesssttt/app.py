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
    args = {}
    # Dog API by Vincent Lin
    URL = 'https://dog.ceo/api/breeds/image/random'
    args['dogs'] = ('Doggos', access_info(URL)['message'])

    # Bored API by Imad Belkbir
    URL = 'https://www.boredapi.com/api/activity'
    args['bored'] = ('Bored', access_info(URL)['activity'])


    # Pokemon API by Tina Wong
    URL_STUB = 'http://api.nytimes.com/svc/topstories/v2/home.json?api-key='
    API_KEY = 'a0232fcf73d345d5901d4f850939650b'
    args['nytimes'] = ('New York Times Top Stories', access_info(URL_STUB, API_KEY)['results'][0])


    return render_template('index.html', **args)

def access_info(URL_STUB, API_KEY = None):
    '''
    Helper to access the info for a URL. Returns the JSON.
    Params: URL_STUB, API_KEY = None
    '''
    if API_KEY:
        URL = URL_STUB + API_KEY
    else:
        URL = URL_STUB
    response = request.urlopen(URL)
    response = response.read()
    info = json.loads(response)
    print(info)
    return info

if __name__ == '__main__':
    app.debug=True
    app.run()

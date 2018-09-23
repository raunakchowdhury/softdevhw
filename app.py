# Raunak Chowdhury
# Softdev1 pd8
# K#09: Solidify
#2018-09-20

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"
    
if __name__ == "__main__":
    app.debug=True
    app.run()

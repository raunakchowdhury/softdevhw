# Raunak Chowdhury, Thomas Zhao
# Softdev1 pd8
# K14 -- Do I Know You?
# 2018-10-01

from flask import Flask, render_template, session, url_for, redirect, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32) #creates key to encode cookies

existing_users = {'chowder' : 'zhao'} # dict for {username: password}

@app.route('/')
def index():
    if 'chowder' in session: #if chowder in session, load welcome, else load login
        return render_template('welcome.html')
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    if request.form['user'] in existing_users: #if username exists
        if existing_users['chowder'] == request.form['pass']: #if username matches existing password
            session['chowder'] = 'zhao' #add to session
            return redirect(url_for('index')) #will load welcome root page
        else:
            return render_template('error.html', error_msg = 'Invalid password!') #these are errors
    return render_template('error.html', error_msg = 'Invalid username!')

@app.route('/logout')
def log_out():
    session.pop('chowder') #remove chowder from session
    #print(session)
    return redirect(url_for('index')) #send back to root


if __name__ == '__main__':
    app.debug = True
    app.run()

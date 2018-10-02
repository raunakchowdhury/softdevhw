# Raunak Chowdhury
# Softdev1 pd8
# K# 14:  text
#2018- ##- ##

from flask import Flask, render_template, session, url_for, redirect, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

existing_users = {'chowder' : 'zhao'} # dict for {username: password}

@app.route('/')
def index():
    if 'chowder' in session:
        return render_template('welcome.html')
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    if request.form['user'] in existing_users:
        if existing_users['chowder'] == request.form['pass']:
            session['chowder'] = 'zhao'
            return redirect(url_for('index'))
        else:
            return render_template('error.html', error_msg = 'Invalid password!')
    return render_template('error.html', error_msg = 'Invalid username!')

@app.route('/logout')
def log_out():
    session.pop('chowder')
    print(session)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()

#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello testlab!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')

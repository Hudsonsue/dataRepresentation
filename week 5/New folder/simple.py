#!flask/bin/python
from flask import flask
 
@app.route('/')
def index():
    return "Hello, World!"
 
if __name__ == '__main__' :
    app.run(debug= True)

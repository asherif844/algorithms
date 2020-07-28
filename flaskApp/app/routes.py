from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ahmed'}

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
        ,
        {
            'author': {'username': 'Mehdi'},
            'body': 'I cannot believe they released the #Snydercut'
        }
    ]
    return render_template('index.html',  user = user, title ='Home', posts = posts)
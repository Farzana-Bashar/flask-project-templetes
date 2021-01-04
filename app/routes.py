from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={"username": "Zerin"}
    posts=[
        {
            "author":{"username":"john"},
            "body":'Beautiful day in chittagong!'
        },
        {
            "author":{"username":"susan"},
            "body":'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

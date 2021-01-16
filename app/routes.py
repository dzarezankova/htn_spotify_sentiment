from flask import render_template
from app import app


@app.route('/index')
def index():
    return "Hello, World!"
    user = 'Listener'
    return render_template('index.html', user=user)

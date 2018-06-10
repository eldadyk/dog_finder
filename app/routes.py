from flask import render_template
from app import app
from app.forms import LoginForm

# ...

@app.route('/login')
def login():
    form = LoginForm()
    print(type(form))
    return render_template('login.html', title='Sign In', form=form)
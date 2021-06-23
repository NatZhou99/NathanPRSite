from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    projects = [
        {
            'author': 'Nathan',
            'projectTitle': 'Some crazy Title',
            'projectSubtitle': 'Project 1 is about this.'
        },
        {
            'author': 'Nathan, Person 2',
            'projectTitle': 'Another Bobastic Title',
            'projectSubtitle': 'Project 2 is about that.'
        }
    ]
    return render_template('index.html', title='Home',projects=projects)




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/resume')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/resume')
def resume():
    author = {'author': 'Nathan'}
    return render_template('resume.html', title='Home', user=author)

    
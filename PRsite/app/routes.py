from flask import render_template, url_for
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/home')
def home():
    
    return render_template('home.html', name=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.first()
        if not user.check_password(form.password.data):
            flash('Invalid password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('resume')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/resume')
@login_required
def resume():
    author = {'author': 'Nathan'}
    return render_template('resume.html', title='Home', user=author)

    
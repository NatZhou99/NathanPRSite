from flask import render_template, url_for, flash
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
    insert="Nathan Zhou"
    subheading="A simple website to show off my projects"
    active=[True, False] #[Home, Projects, Resume]
    return render_template('home.html', insert=insert, subheading=subheading, active=active)


@app.route('/projects')
def projects():
    insert="Project Listings"
    subheading="List of all completed projects"
    active=[False, True] #[Home, Projects, Resume]
    return render_template('projects.html', insert=insert, subheading=subheading, active=active)


@app.route('/login', methods=['GET', 'POST'])
def login():
    active=[False, False]
    insert="Password Please"
    subheading=""
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

    return render_template('login.html', title='Password Please',insert=insert, subheading=subheading,  form=form, active=active)


@app.route('/resume')
@login_required
def resume():
    active=[False, False]
    insert="My Resume"
    subheading=""
    return render_template('resume.html', title='Resume',insert=insert,subheading=subheading, active=active)

    
################################################## Projects ##################################################

@app.route('/dry_bean')
def dry_bean():
    active=[False, True]
    insert="Dry Bean Dataset Analysis"
    iframe="https://www.kaggle.com/embed/alasunghainian/dry-bean-dataset?kernelSessionId=69027927" 
    return render_template('baseproject.html', 
                            insert=insert, 
                            iframe=iframe,
                            active=active)
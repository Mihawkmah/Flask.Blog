# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, request, flash
from app import app, db, lm
from flask.ext.login import current_user, login_user, logout_user, login_required
from app.models import Posts, User
from app.forms import LoginForm

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    paginator = Posts.objects.paginate(page=page, per_page=12)
    return render_template('index.html', paginator=paginator)

@app.route('/post/<string:post_id>')
def get_post(post_id):
    post = Posts.objects(id=post_id).first()
    return render_template('post.html',post=post)

@app.route('/editor')
@login_required
def editor():
    return render_template('editor.html')

@lm.user_loader
def user_loader(userid):
    user = User.objects(_id=userid).first()
    return user

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        user = User.objects(username=username).first()
        if not user:
            flash('用户名错误')
        elif password != user.password:
            flash('密码错误')
        else:
            login_user(user)
            return redirect(url_for('editor'))
    return render_template('login.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

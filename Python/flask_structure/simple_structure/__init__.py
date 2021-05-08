#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='statics', static_url_path='/static')

from .views.account import account
from .views.blog import blog
from .views.user import user

app.register_blueprint(account)
app.register_blueprint(blog)
app.register_blueprint(user)

app.num = 0


@app.before_request
def temp11():
    app.num = app.num + 1
    print('app.num before_request', app.num)
    return


@app.after_request
def temp11(response):
    app.num = app.num + 1
    print('app.num after_request', app.num)
    return response


@app.route('/numzero')
def temp23():
    app.num = 0
    print('app.num numzero', app.num)
    return ''

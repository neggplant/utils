#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template, request

account = Blueprint('account', __name__)


@account.route('/login.html', methods=['GET', "POST"])
def login():
    return render_template('login.html')

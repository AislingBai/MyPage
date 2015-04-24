# coding=utf8
from . import main
from flask import redirect, render_template, url_for, request


@main.route('/')
def index():
    a = " Aisling Bai's homepage "
    name = u'白娟娟'
    return render_template('main/homepage.html', a=a)
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mongoengine import MongoEngine
from flask.ext.login import LoginManager

# 初始化flask应用
app = Flask(__name__)
app.config.from_object('config')

# 初始化数据库
app.config['MONGODB_SETTINGS'] = {
    'db': 'mblog',
    'host': '127.0.0.1',
    'port': 27017
}
db = MongoEngine(app)

# 初始化Flasklogin
lm = LoginManager(app)

from app import views,models

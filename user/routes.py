from flask import Flask
from login import app
from user.models import User

@app.route('/user/login/', methods=['POST'])
def signin():
    return User().login()

@app.route('/user/signout/')
def signout():
    return User().signout()

@app.route('/admin/findUser/', methods=['POST'])
def findUser():
    return User().get_user()

@app.route('/admin/saveUser/', methods=['POST'])
def saveUser():
    return User().save_user()

@app.route('/admin/deleteUser/', methods=['POST'])
def deleteUser():
    return User().delete_user()

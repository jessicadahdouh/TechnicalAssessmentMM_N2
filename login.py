from flask import Flask, render_template,session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = pymongo.MongoClient('localhost', 27017)
db = client.user_login

# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            print("You need to login first")
            return redirect('/')

    return wrap


# Routes
from user import routes

@app.route('/')
def initialize():
    return render_template('login.html')

@app.route('/admin/')
@login_required
def admin():
    return render_template('admin.html')

@app.route('/user/')
@login_required
def user():
    return render_template('user.html')

# @app.route('/admin/findUser/')
# def user():
#     result = routes.findUser()
#     return render_template('admin.html', result)

# import json
# import logging
# import requests
# from flask import Flask, request, render_template, redirect, flash, url_for
# from flask import session, make_response, g
# from flask import current_app
# from flask import request

# from keycloak_utils import get_admin, create_user, get_oidc, get_token, check_token


# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)
# app.config.from_object('settings')
# # app.config.from_envvar('KEYCLOAK_FLASK_SETTINGS')


# @app.before_request
# def load_user():
#     g.username = session.get('username')
#     g.access_token = session.get('access_token')


# @app.route('/')
# def initialize():
#     return render_template('login.html')


# @app.route('/user/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         print("--------------", username + "passsss    " + password)
#         oidc_obj = get_oidc()
#         token = get_token(oidc_obj, username, password)
#         print("\nTOKEN: %s\n" % token)
#         # response = make_response(redirect(url_for('initialize')))
#         # if token:
#         #     response.set_cookie('access_token', token['access_token'])
#         #     session['access_token'] = token['access_token']
#         #     session['username'] = username
#         # return response
#     return render_template('login.html')


# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     session.pop('access_token', None)
#     return redirect(url_for('home'))


# @app.route('/headers')
# def headers():
#     return dict(request.headers)


# @app.route('/protected')
# def protected():
#     ingress_host = current_app.config.get('INGRESS_HOST')
#     resp = 'Forbidden!'
#     access_token = session.get('access_token')
#     if access_token:
#         if check_token(access_token):
#             headers = {'Authorization': 'Bearer ' + access_token}
#             r = requests.get(ingress_host, headers=headers)
#             resp = 'Protected resource is accessible. Yay! Here is the response: %s' % str(r.text)
#     return resp

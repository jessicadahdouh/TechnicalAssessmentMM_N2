import json
from flask import Flask, session, jsonify, render_template, request, redirect, url_for
from login import db

class User:

    def login(self):
        username = request.form.get('username')
        password = request.form.get('password')
        user = db.users.find_one({
            "name": username
        })
        # checking if user is found  => right credentials
        if user is not None:
            # creating session for user
            del user['password']
            session['logged_in'] = True
            session['user'] = username
            
            # checking if user is admin
            if user['is_admin']:
                return jsonify({'auth':True,'is_admin': True})
            else:
                return jsonify({'auth':True,'is_admin': False}) 
        else:
            return jsonify({'auth':False})


    def signout(self):  
        session.clear()
        return redirect('/')

    def get_user(self):
        username = request.form.get('username')
        user = db.users.find_one({
            "name": username
        })
        # checking if value is found
        if user is not None:
            return jsonify({'userFound':user['name']})
        else:
            return jsonify({'userFound':'User not found'})

    def save_user(self):
        username = request.form.get('username')
        newUser = request.form.get('newuser')

        oldUser = db.users.find_one({
            "name": username
        })

        user = db.users.find_one({
            "name": newUser
        })
        # checking if value is found
        if user is not None:
            return jsonify({'userFound':'User already exists','exists': True})
        else:
            print(oldUser["_id"])
            oldValues = { "_id": oldUser["_id"] }
            newValues = { "$set": { "name": newUser } }
        
            db.users.update_one(oldValues, newValues)
            return jsonify({'userFound':'Update successful','exists':False})
    
    
    def delete_user(self):
        username = request.form.get('username')

        user = db.users.find_one({
            "name": username
        })

        db.users.delete_one({"_id": user['_id']})
        return jsonify({'userFound':'User has been deleted'})
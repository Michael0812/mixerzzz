import os
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo, pymongo


app = Flask(__name__)

# Configuration of database
app.config["MONGO_DBNAME"] = 'whiskyDB'
app.config["MONGO_URI"] = "mongodb+srv://Michael0812:a7d2hp@myfirstcluster-2ro3f.mongodb.net/whiskyDB?retryWrites=true&w=majority";


mongo = PyMongo(app)


# Home page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('pages/index.html')


# Drinks page
@app.route('/drinks.html')
def drinks():
    return render_template('pages/drinks.html', tasks=mongo.db.tasks.find())

# Register page
@app.route('/register.html')
def register():
    return render_template('pages/register.html')


# Login page
@app.route('/login.html')
def login():
    return render_template('pages/login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
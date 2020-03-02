import os
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo, pymongo


app = Flask(__name__)

# Configuration of database
app.config["MONGO_DBNAME"] = 'whiskyDB'
app.config["MONGO_URI"] = "mongodb+srv://Michael0812:a7d2hp@myfirstcluster-2ro3f.mongodb.net/whiskyDB?retryWrites=true&w=majority"


mongo = PyMongo(app)


# Home page

@app.route('/index.html')
def index():
    return render_template('pages/index.html')


# Drinks page
@app.route('/drinks.html')
def drinks():
    return render_template('pages/drinks.html', whisky=mongo.db.whisky.find())

# Register page
@app.route('/register.html')
def register():
    return render_template('pages/register.html')


# Login page
@app.route('/login.html')
def login():
    return render_template('pages/login.html')

# Add page
@app.route('/')
@app.route('/add_whisky')
def add_whisky():
    return render_template('pages/addwhisky.html',
    categories=mongo.db.categories.find())


@app.route('/insert_whisky', methods=['POST'])
def insert_whisky():
    whisky = mongo.db.whisky
    whisky.insert_one(request.form.to_dict())
    return redirect(url_for('drinks'))

# Edit whisky
@app.route('/edit_whisky/<whisky_id>')
def edit_whisky(whisky_id):
    the_whisky =  mongo.db.whisky.find_one({"_id": ObjectId(whisky_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editwhisky.html', whisky=the_whisky,
                           categories=all_categories)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
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
@app.route('/')
def index():
    return render_template('pages/index.html')


# Drinks page
@app.route('/drinks')
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
@app.route('/drink/add')
def add_whisky():
    return render_template('pages/addwhisky.html',
    categories=mongo.db.categories.find())


@app.route('/drink/insert', methods=['POST'])
def insert_whisky():
    whisky = mongo.db.whisky
    whisky.insert_one(request.form.to_dict())
    return redirect(url_for('drinks'))

# Edit whisky
@app.route('/drink/edit/<whisky_id>')
def edit_whisky(whisky_id):
    the_whisky =  mongo.db.whisky.find_one({"_id": ObjectId(whisky_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('pages/editwhisky.html', whisky=the_whisky,
                           categories=all_categories)

# Update whisky
@app.route('/drink/update/<whisky_id>', methods=["POST"])
def update_whisky(whisky_id):
    whisky = mongo.db.whisky
    whisky.update( {'_id': ObjectId(whisky_id)},
    {
        'category_name': request.form.get('category_name'),
        'whisky_img': request.form.get('whisky_img'),
        'whisky_name': request.form.get('whisky_name'),
        'whisky_description': request.form.get('whisky_description'),
        'number_water': request.form.get('number_water'),
        'number_ginger': request.form.get('number_ginger'),
        'number_coke': request.form.get('number_coke'),
        'number_green_tea': request.form.get('number_green_tea')
    })
    return redirect(url_for('drinks'))


# Delete whisky
@app.route('/drink/delete/<whisky_id>')
def delete_whisky(whisky_id):
    mongo.db.whisky.remove({'_id': ObjectId(whisky_id)})
    return redirect(url_for('drinks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
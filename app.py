import os
from flask import Flask, render_template, redirect, flash, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo, pymongo
from os import path


if path.exists('env.py'):
  import env 


app = Flask(__name__)


# Configuration of database
app.config['MONGODB_NAME'] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = 'secret'

mongo = PyMongo(app)


# Home page
@app.route('/')
def index():
    """Home Page - That page contains all important information for user"""
    return render_template('pages/index.html')


# Drinks page
@app.route('/drinks')
def drinks():
    """Drinks Page - display all items stored in MongoDB / On that page users can READ, EDIT & DELETE"""
    return render_template('pages/drinks.html', whiskys=mongo.db.whisky.find())


# Add page
@app.route('/drink/add')
def add_whisky():
    """ Add Page - On that page, users are allowed to easily add new item(drink). Item is going to be add on the page and in database. Also, user are required to fill up all forms"""
    return render_template('pages/addwhisky.html',
            categories=mongo.db.categories.find())


@app.route('/drink/insert', methods=['POST'])
def insert_whisky():
    """"""
    whisky = mongo.db.whisky
    whisky.insert_one(request.form.to_dict())
    return redirect(url_for('drinks'))


# Edit whisky
@app.route('/edit/<whisky_id>')
def edit_whisky(whisky_id):
    """Edit Page - on that page user are allowed to edit specific item. 
    All changes going to be change on the Drink Page and database"""
    the_whisky =  mongo.db.whisky.find_one({"_id": ObjectId(whisky_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('pages/editwhisky.html', whisky=the_whisky,
                           categories=all_categories)


# Update whisky
@app.route('/drink/update/<whisky_id>', methods=["POST"])
def update_whisky(whisky_id):
    """Update - user are allowed to click 'update', after editing in Edit page.
    That will approve all changes. The changes will be saved on the page and database(MongoDB)
    and redirect user to drink page, where user can see changes"""
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
    """Delete - user are allowed to delete specific item(drink) using button(delete) 
    that is located on drink page under every item.
    Item, is going to be delete from the page and database(MongoDB)
    """
    mongo.db.whisky.remove({'_id': ObjectId(whisky_id)})
    return redirect(url_for('drinks'))


# Contact page
@app.route('/contact')
def contact():
    """Contact Page - user can easily contact with admin sending a message to him.
    Also, user can choose if he wants to getting newsletter"""
    return render_template('pages/contact.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
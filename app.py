import os
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'whiskyDB'
app.config["MONGO_URI"] = "mongodb+srv://Michael0812:a7d2hp@myfirstcluster-2ro3f.mongodb.net/whiskyDB?retryWrites=true&w=majority"



@app.route('/')
def index():
    return render_template('pages/index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
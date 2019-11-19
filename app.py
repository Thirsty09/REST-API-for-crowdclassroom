from flask import Flask, render_template, redirect, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

#init app
app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db -- sqlalchemy
db = SQLAlchemy(app)
# Init ma -- Marshmallow
ma = Marshmallow(app)


# Crowdclassroom classes
class Classroom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), unique=True, nullable=False)
    action = db.Column(db.String(256))
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, url, action):
        self.url = url
        self.action = action

# The Schema
class ClassSchema(ma.Schema):
    class Meta:
        fields = ('id', 'url', 'action', 'post_date')

# Init schema
class_schema = ClassSchema() # one object
classes_schema =  ClassSchema(many=True) # Many Objects

## Routes
@app.route('/')
def index():
    return 'Api Tutorial' + temp

 # Create a Class   
@app.route('/class', methods=['POST'])
def create_class():
    url = request.json['url']
    action = request.json['action']

    new_class = Classroom(url, action)

    db.session.add(new_class)
    db.session.commit()

    return class_schema.jsonify(new_class)

# Get All Classes
@app.route('/class', methods=['GET'])
def get_classes():
    all_classes = Classroom.query.all()
    result = classes_schema.dump(all_classes) # for an array only
    return jsonify(result)

# Get Single Classes
@app.route('/class/<id>', methods=['GET'])
def get_class(id):
    single_class = Classroom.query.get(id) # fetching the particular class
    return class_schema.jsonify(single_class)

 # Update a Class   
@app.route('/class/<id>', methods=['PUT'])
def update_class(id):
    single_class = Classroom.query.get(id)

    url = request.json['url']
    action = request.json['action']

    # Constructing new product to subt to the DB in place of the old product with the given id
    single_class.url = url
    single_class.action = action

    db.session.commit()

    return class_schema.jsonify(new_class)

# Delete Class
@app.route('/class/<id>', methods=['DELETE'])
def delete_class(id):
    single_class = Classroom.query.get(id) # fetching the particular class
    db.session.delete(single_class)
    db.session.commit() # committing the delete, to take effect
    return class_schema.jsonify(single_class)


if __name__ == '__main__':
    app.run(debug=True)


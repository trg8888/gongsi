from flask import Flask
import click
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from datetime import datetime


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = False
app.config['SECRET_KEY'] = 'tasd2sadsadsad'
db = SQLAlchemy(app)

@app.cli.command()
def initdb():
    db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


class Writer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70),unique=True)
    note = db.Column(db.String(70),unique=False)
    jiontime = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    books = db.relationship('Book', back_populates='writer')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    jiontime = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    note = db.Column(db.String(70),unique=False)
    state = db.Column(db.Boolean,default=True, unique=False)
    writer_id = db.Column(db.Integer, db.ForeignKey('writer.id'))
    writer = db.relationship('Writer', back_populates='books')
    quantity = db.relationship('Quantity',back_populates='book')

class Quantity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=True, unique=True)
    description = db.Column(db.Text)
    attribute = db.Column(db.String(150))
    picture = db.Column(db.String(150))
    price = db.Column(db.Float(5,2))
    jiontime = db.Column(db.DateTime,default=datetime.utcnow, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    book = db.relationship('Book',back_populates='quantity')
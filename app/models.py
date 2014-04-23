# from hashlib import md5
from mixins import CRUDMixin
from flask.ext.login import UserMixin
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
# import flask.ext.whooshalchemy as whooshalchemy

ROLE_USER = 0
ROLE_ADMIN = 1

class User(UserMixin, CRUDMixin,  db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))
    
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    db = db.relationship('Database', backref='user', lazy='dynamic')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.password = password

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_admin(self):
        if self.role > 0:
            return True
        else:
            return False

    def __repr__(self):
        return '<User %r>' % (self.name)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    survey1_id = db.Column(db.Integer, db.ForeignKey('survey1.id'))
    survey2_id = db.Column(db.Integer, db.ForeignKey('survey2.id'))
    survey3_id = db.Column(db.Integer, db.ForeignKey('survey3.id'))
    survey4_id = db.Column(db.Integer, db.ForeignKey('survey4.id'))

    name = db.Column(db.String(255), unique = True)

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Survey1(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    education = db.Column(db.Integer)
    language = db.Column(db.String(20))
    db = db.relationship('Database', backref='survey1', lazy='dynamic')

class Survey2(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    major = db.Column(db.Integer)
    department = db.Column(db.String(30))
    count = db.Column(db.Integer)
    unique = db.Column(db.Integer)
    db = db.relationship('Database', backref='survey2', lazy='dynamic')

class Survey3(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #select multiple field
    #select multiple field
    modify = db.Column(db.Integer)
    usedPassword = db.Column(db.Integer)
    #select multiple field
    #select multiple field
    #select multiple field
    db = db.relationship('Database', backref='survey3', lazy='dynamic')

class Survey4(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    computerTime = db.Column(db.Integer)
    # passwordCreation = db.Column()
    storePasswords = db.Column(db.Integer)
    # howStored
    comments = db.Column(db.String)


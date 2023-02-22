from .import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
class Usermachines(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userid=db.Column(db.Integer,db.ForeignKey("user.id"))
    machineid=db.Column(db.Integer,db.ForeignKey("machines.id"))

class machines(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30))

#class Allexcercises(db.Model):
#    id=db.Column(db.Integer, primary_key=True)
#    machine=db.Column(db.String(10000),db.ForeignKey("machines.machine"))
#    excercise=db.Column(db.String(10000),unique=True)

class Plans(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    excercise=db.Column(db.String(10000))
    plan_no=db.Column(db.Integer)
    #date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))


    
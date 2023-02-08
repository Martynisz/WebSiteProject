from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import select, text, create_engine
from sqlalchemy.orm import Session
from .import db, DB_NAME
from .models import User, Usermachines
views=Blueprint("views",__name__)

@views.route('/')
def home():
    return render_template("about.html",user=current_user)

@views.route('/menu')
@login_required
def menu():
    return render_template("menu.html",user=current_user,uname=current_user.first_name)

@views.route('/machines',methods=['get','post'])
@login_required
def machines():
    if request.method=="POST":
        print(request.form.getlist('multiselect'))
        addtousermachines(request.form.getlist('multiselect'))
        return redirect(url_for("views.menu"))

    return render_template("machines.html",user=current_user,machines=listfromdb())





#-----------------------------------------------------------------------------

def listfromdb():
    result=db.session.execute("SELECT * FROM machines;")
    from collections import namedtuple
    dictionary={}
    Record = namedtuple('Record', result.keys()) #tupla z całego wiersza db 
    records = [Record(*r) for r in result.fetchall()]
    for r in records:
        dictionary.update({r.id:r.name})
        print(dictionary[r.id])
    #for r in result:
    #    print(r[0]) # Access by positional index
    #    print(r['first_name']) # Access by column name as a string
    #    r_dict = dict(r.id()) # convert to dict keyed by column names
    return dictionary
def addtousermachines(lista):
    for i in lista:
        print(i)
        new_use_machine=Usermachines(userid=current_user.id,machineid=i)
        db.session.add(new_use_machine)
        db.session.commit()
        






#def Addmachines():
#    new_user=User(email=email,first_name=firstname,password=generate_password_hash(password,"sha256"))
#    db.session.add(new_user)
#    db.session.commit()
#    flash("haslo,mail,nazwa prawidlowe --> konto utworzone",category="success")
#    return new_user
#def returnmachinesform():
    
    #machinesfile=open("static/machines_existing.txt")
    #machines_existing=machinesfile.read()
    #machinesfile.close
    #machinesform=swapletter(machines_existing," ","_")
    #machinesform=machinesform.split(";")
    

    #return machinesform

def swapletter(swapabletxt,leterstoswap,swapwith):
        i=1
        swapped=""
        for leter in swapabletxt:
            if leter==leterstoswap:
                swapped=swapped+swapwith
            else:
                swapped=swapped+leter
            i=i+1
        return swapped

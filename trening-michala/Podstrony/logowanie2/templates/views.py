from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
views=Blueprint("views",__name__)

@views.route('/')
def home():
    return render_template("about.html",user=current_user)

@views.route('/menu')
@login_required
def menu():
    return render_template("menu.html",user=current_user)

@views.route('/machines',methods=['get','post'])
@login_required
def machines():
    if request.method=="POST":
        print(request.form.lists)
        
        return redirect(url_for("views.menu"))

    return render_template("machines.html",user=current_user,machines=returnmachinesform())





#-----------------------------------------------------------------------------











def Addmachines():
    new_user=User(email=email,first_name=firstname,password=generate_password_hash(password,"sha256"))
    db.session.add(new_user)
    db.session.commit()
    flash("haslo,mail,nazwa prawidlowe --> konto utworzone",category="success")
    return new_user
def returnmachinesform():
    
    machinesfile=open("static/machines_existing.txt")
    machines_existing=machinesfile.read()
    machinesfile.close
    machinesform=swapletter(machines_existing," ","_")
    machinesform=machinesform.split(";")
    

    return machinesform

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
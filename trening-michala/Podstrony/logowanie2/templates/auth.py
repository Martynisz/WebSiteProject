from flask import Flask, Blueprint, render_template, Request, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth=Blueprint("auth",__name__)

@auth.route("/login", methods=['get','post'])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        if login_check(email, password):
            user=User.query.filter_by(email=email).first()
            login_user(user,remember=True)
            return redirect(url_for("views.home"))

    return render_template("login.html", text="testing",user=current_user,bolean=True)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign_up", methods=['get','post'])
def sign_up():
    if request.method=="POST":
        
        email=request.form.get("email")
        firstname=request.form.get("name")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        if check_email(email) & pass_check(password1,password2) & name_check(firstname):
            create_new_user(email,password1,firstname)
            login_user(user,remember=True)
            return redirect(url_for('views.home'))
        

    
    return render_template("sign_up.html", user=current_user)

def check_email(email):
    warun=True
    user=User.query.filter_by(email=email).first()
    if user:
        flash("this email exists on site already",category="error")
        warun=False
    return warun
def name_check(name):
    warun=True
    if len(name)<3:
        flash("your name must be at least 3 characters long",category="error")
        warun=False
    return warun
def pass_check(password,password1):
    znakispecjalne="!@#$%^&*()_+=?>.<;/"
    warun=True
    if len(password)<6:
        flash("your password must be at least 6 characters long",category="error")
        warun=False
    elif not any(i.isupper() for i in password ):
        flash("your password must contain at least one UPPERCASE",category="error")
        warun=False
    elif not any(i in znakispecjalne for i in password ):
        flash("your password must contain at least one special character",category="error")
        warun=False
    elif password!=password1:
        flash("your passwords dont match",category="error")
        warun=False
    return warun
def create_new_user(email,password,firstname):
    new_user=User(email=email,first_name=firstname,password=generate_password_hash(password,"sha256"))
    db.session.add(new_user)
    db.session.commit()
    flash("haslo,mail,nazwa prawidlowe --> konto utworzone",category="success")
    return True
def login_check(email,password):
    user=User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password,password):
            flash("loged in succesfully", category="success")
            return True
        else:
            flash("wrong password", category="error")
            return False
    else:
        flash("no such email found", category="error")
        return False

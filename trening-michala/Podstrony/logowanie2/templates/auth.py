from flask import Blueprint, render_template, Request, request, flash

auth=Blueprint("auth",__name__)

@auth.route("/login", methods=['get','post'])
def login():
    data=request.form
    print(data)
    return render_template("login.html", text="testing",user="michu",bolean=True)
@auth.route("/logout")
def logout():
    return "<p>logout</p>"
@auth.route("/sign_up", methods=['get','post'])
def sign_up():
    if request.method=="POST":
        
        email=request.form.get("email")
        firstname=request.form.get("name")
        password1=request.form.get("password1")
        password2=request.form.get("password2")
        if check_email(email) & pass_check(password1,password2) & name_check(firstname):
            flash("haslo,mail,nazwa prawidlowe --> konto utworzone",category="success")
        pass

    
    return render_template("sign_up.html")
def check_email(email):
    warun=True
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
    if not any(i.isupper() for i in password ):
        flash("your password must contain at least one UPPERCASE",category="error")
        warun=False
    if not any(i in znakispecjalne for i in password ):
        flash("your password must contain at least one special character",category="error")
        warun=False
    if password!=password1:
        flash("your passwords dont match",category="error")
        warun=False
    return warun
from flask import Blueprint, render_template, Request, request

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
        pass

    
    return render_template("sign_up.html")
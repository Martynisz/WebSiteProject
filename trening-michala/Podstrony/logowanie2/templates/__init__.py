from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import path
from flask_login import LoginManager
db=SQLAlchemy()
DB_NAME="database.db"
def create_app(__name__):
    app=Flask(__name__,template_folder="templates")
    app.config["SECRET_KEY"]="ASDASDSADASD"
    app.config["SQLALCHEMY_DATABASE_URI"]=f'sqlite:///{DB_NAME}'
    engine=create_engine(app.config["SQLALCHEMY_DATABASE_URI"],echo=True)
    db.metadata.create_all(bind=engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User,Plans,Usermachines
    with app.app_context():
        db.create_all()
        print("created database")
    
    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))   
    return app
#create_database(app)
#def create_database(app):
    #if not path.exists("logowanie2/" + DB_NAME):
        #db.create_all(app=app)
        #print("created database")
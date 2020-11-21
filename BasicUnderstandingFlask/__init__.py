from flask import Flask,Blueprint
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app=Flask(__name__)
app.config["SECRET_KEY"]="Chivo"
Base_Dir=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(Base_Dir,'sqlite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="basics.Flasklogin"
from BasicUnderstandingFlask.views import basic_buleprint
app.register_blueprint(basic_buleprint,url_prefix='/blueprint')



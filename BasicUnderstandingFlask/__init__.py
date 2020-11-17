from flask import Flask,Blueprint
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SECRET_KEY"]="Chivo"
Base_Dir=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(Base_Dir,'sqlite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)

from BasicUnderstandingFlask.views import basic_buleprint
app.register_blueprint(basic_buleprint,url_prefix='/blueprint')



from flask import Flask,render_template,url_for,request,redirect,make_response,session
from forms import MyFirstBasicForm,postform
from flask_migrate import Migrate
import os
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User
from models import comments
from models import Post
app=Flask(__name__)
app.app_context().push()
db.init_app(app)
# db=SQLAlchemy(app)
app.config["SECRET_KEY"]="Chivo"
Base_Dir=os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(Base_Dir,'sqlite.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.create_all()
migrate = Migrate(app, db)
# print(User.query.filter_by(username="Flask1"))
# users=User.query.all()[0]
# print(users.password)
# user1=User.query.get(1)
# print(user1)
def create():
    p1=Post(title="Sriram's blog",description="sriram@dvb.com is his email")
    print(user1.id)
    p1.user_id=user1.id
    db.session.add(p1)
    db.session.commit()
    return "Success"
# create()
# random=user1.posts[0].description
# random=User.query.join(Post).all()
# print(random)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    form=MyFirstBasicForm()
    if request.method=="POST":
        if form.validate_on_submit():
            fname=form.Name.data
            session["name"]=fname
            session["email"]=form.Email.data
            return redirect(url_for("showallposts",name=fname))
        else:
            pass
    resp=make_response(render_template("signup.html",form=form))
    resp.set_cookie('username', 'the username')
    return resp
@app.route("/start/<string:fname>",methods=['GET','POST'])
def start(fname):
    if request.method=="POST":
        list_of_ans=request.form.getlist("lang")
        print(list_of_ans)
    return render_template("welcome.html",name=fname)
@app.route("/save" , methods=['GET'])
def save():
    return url_for("home")

@app.route("/<string:name>/allposts",methods=['GET','POST'])
def showallposts(name):
    form=postform()
    if request.method=="POST":
        print(form)
        print(form.title.data)
        print(form.description.data)
        if form.validate_on_submit():
            title=form.title.data
            # print(title)
            description=form.description.data
            # print(description)
            getuserid=User.query.filter(User.username==name)[0].id
            # print(getuserid)
            p=Post(title=title,description=description,user_id=getuserid)
            db.session.add(p)
            db.session.commit()
            form.description.data=''
            form.title.data=''
        else:
            print(form.errors)
    getallposts=Post.query.all()
    # print(getallposts)
    return render_template("allposts.html",allposts=getallposts,form=form)
if __name__ == "__main__":
    app.run(debug=True)
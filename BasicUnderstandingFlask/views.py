from flask import Flask,render_template,url_for,request,redirect,make_response,session,Blueprint,current_app
from .forms import MyFirstBasicForm,postform
from BasicUnderstandingFlask import db,app
from .models import User,comments,Post
from flask_login import login_required,login_user,logout_user

basic_buleprint= Blueprint("basics",__name__,
                            template_folder='templates\FlaskBasics')
with app.app_context():
    print(dir(app))
    print(app.blueprints)
    print(current_app)
    print(current_app.name)
# def create():
#     # p1=Post(title="Sriram's blog",description="sriram@dvb.com is his email")
#     # user1=User.query.get(1)
#     # print(user1.id)
#     # p1.user_id=user1.id
#     p1=User("Chivothboss","Chivo0007@gmail.com","Chivo@07")
#     db.session.add(p1)
#     db.session.commit()
#     return "Success"
# create()

# print(User.query.filter_by(username="Chivothboss")[0].password)
 
@basic_buleprint.route("/signin",methods=['GET','POST'])
def Flasklogin():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        try:
            user=User.query.filter_by(username=username)[0]
            if user.check_password(password):
                login_user(user)
                nexturl=request.args.get("next")
                return redirect(nexturl or url_for("basics.showallposts",name=user.username))
        except:
            return redirect(url_for("basics.signup"))
    return render_template("signin.html")
    # # u1=User.query.get(1)
    # login_user(u1)
    # resp=make_response(redirect(url_for("basics.start",fname=u1.username)))
    # resp.set_cookie('username',u1.username)
    # return resp

@basic_buleprint.route("/signout",methods=['GET','POST'])
def logout():
    logout_user()
    return "Logged Out Successfully"

@basic_buleprint.route("/signup",methods=['GET','POST'])
def signup():
    form=MyFirstBasicForm()
    if request.method=="POST":
        if form.validate_on_submit():
            fname=form.Name.data
            session["name"]=fname
            session["email"]=form.Email.data
            u=User(username=fname,email=form.Email.data,password=form.password.data)
            db.session.add(u)
            db.session.commit()
            return redirect(url_for("basics.start",fname=fname))
        else:
            pass
    resp=make_response(render_template("signup.html",form=form))
    resp.set_cookie('username', 'the username')
    return resp


@basic_buleprint.route("/start/<string:fname>",methods=['GET','POST'])
@login_required
def start(fname):
    try:
        print(request.cookies.get("username"))
        # print(session["user_id"])
        print(session)
        print(session["_user_id"])
    except:
        pass
    if request.method=="POST":
        list_of_ans=request.form.getlist("lang")
        print(list_of_ans)
    return render_template("welcome.html",name=fname)
@basic_buleprint.route("/save" , methods=['GET'])
def save():
    return url_for("home")

@basic_buleprint.route("/<string:name>/allposts",methods=['GET','POST'])
@login_required
def showallposts(name):
    form=postform()
    if request.method=="POST":
        if form.validate_on_submit():
            title=form.title.data
            description=form.description.data
            getuserid=User.query.filter(User.username==name)[0].id
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


#-----------FOr understanding ----------------


# print(User.query.filter_by(username="Flask1"))
# users=User.query.all()[0]
# print(users.password)
# user1=User.query.get(1)
# print(user1)
# random=user1.posts[0].description
# random=User.query.join(Post).all()
# print(random)
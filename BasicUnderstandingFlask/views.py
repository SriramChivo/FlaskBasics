from flask import Flask,render_template,url_for,request,redirect,make_response,session,Blueprint
from .forms import MyFirstBasicForm,postform
from BasicUnderstandingFlask import db
from .models import User,comments,Post


basic_buleprint= Blueprint("basics",__name__,
                            template_folder='templates\FlaskBasics')

def create():
    p1=Post(title="Sriram's blog",description="sriram@dvb.com is his email")
    user1=User.query.get(1)
    print(user1.id)
    p1.user_id=user1.id
    db.session.add(p1)
    db.session.commit()
    return "Success"
# create()


@basic_buleprint.route("/signup",methods=['GET','POST'])
def signup():
    form=MyFirstBasicForm()
    if request.method=="POST":
        if form.validate_on_submit():
            fname=form.Name.data
            session["name"]=fname
            session["email"]=form.Email.data
            return redirect(url_for("basics.showallposts",name=fname))
        else:
            pass
    resp=make_response(render_template("signup.html",form=form))
    resp.set_cookie('username', 'the username')
    return resp


@basic_buleprint.route("/start/<string:fname>",methods=['GET','POST'])
def start(fname):
    if request.method=="POST":
        list_of_ans=request.form.getlist("lang")
        print(list_of_ans)
    return render_template("welcome.html",name=fname)
@basic_buleprint.route("/save" , methods=['GET'])
def save():
    return url_for("home")

@basic_buleprint.route("/<string:name>/allposts",methods=['GET','POST'])
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
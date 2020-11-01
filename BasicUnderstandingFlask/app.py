from flask import Flask,render_template,url_for,request,redirect
from forms import MyFirstBasicForm
app=Flask(__name__)
app.config["SECRET_KEY"]="Chivo"
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup",methods=['GET','POST'])
def signup():
    form=MyFirstBasicForm()
    if request.method=="POST":
        if form.validate_on_submit():
            fname=form.Name.data
            return redirect(url_for("start",fname=fname))
        else:
            pass
    return render_template("signup.html",form=form)
@app.route("/start/<string:fname>")
def start(fname):
    return f"Welcome {fname}, We are happy that you intrested to meet flaskman!!"
@app.route("/save" , methods=['GET'])
def save():
    return url_for("home")


if __name__ == "__main__":
    app.run(debug=True)
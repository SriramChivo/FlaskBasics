# from model_intialize import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
db=SQLAlchemy()
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100))

    def __repr__(self):
        return self.username

    @hybrid_property
    def get_email(self):
        return self.email


# associateTable=db.table(
#     db.Column("post_id",db.Integer,db.ForeignKey("post.id")),
#     db.Column("comments_id",db.Integer,db.ForeignKey("comments.id"))
# )

class Post(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.String(500),nullable=False)
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'))
    users=db.relationship('User',backref="posts",lazy=True)
    # comments=db.relationship('comments',secondary="associateTable",lazy=True,
    #                         backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return self.title



class comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    comments_description=db.Column(db.String(150),nullable=False)

    def __repr__(self):
        return self.comments_description[20]




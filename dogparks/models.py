from dogparks import login_manager, db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


    # Authentication route made possible by.
from flask_login import UserMixin
    #^^Remember to pip3 install this. 



    # The user_loader decorator allows flask-login to load the current user
    # and grab their id.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

    #SETTING UP DATABASE, MODELING 1. USER AND BLOG.
    #USER WILL HAVE A PRIMARY_KEY ID (AUTO)
    #  




class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    

    #foreign key Stuff:
    posts = db.relationship('Posts', backref='author', lazy=True)
  
    #^ the author can be referenced in Templates. 

    def __init__(self, email, username, password):
        
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    #^^CHECK TO MAKE SURE THIS IS WORKING

    def __repr__(self):
        return f"UserName: {self.username}"





class Posts(db.Model):
    users = db.relationship(User)
    #called users, can't use user because of class name. 

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    #^^FOREIGNKEY, ONE TO MANY. ONE USER TO MANY POST. 
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)











    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id =user_id























    def __repr__(self):
        return f"Post Id: {self.id} --- Date: {self.date} --- Title: {self.title}"

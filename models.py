from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy import false

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Class for user."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), nullable = false, unique = True)
    email = db.Column(db.String, nullable = false, unique = True)
    password = db.Column(db.String, nullable = False)
    bio = db.Column(db.String)
    friend_code = db.Column(db.String(12))
    dream_code = db.Column(db.String(12))
    image_url = db.Column(db.String)

    @classmethod
    def signin(cls, username, password):
        """Validate user on sign in. 
        Return user if password is valid, else return false."""
        
        user = User.query.filter_by(username = username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False
    
    @classmethod
    def signup(cls, username, password, email):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username = username, password = hashed_utf8, email = email)

class Villager(db.Model):
    """Class to store villagers each island has."""
    __tablename__ = "villagers"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    image_url = db.Column(db.String, nullable = False)

class Island(db.Model):
    """Class to store villagers each island has."""
    __tablename__ = "islands"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    villager_id = db.Column(db.Integer, db.ForeignKey("villagers.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    users = db.relationship("User", backref = "islands")
    villagers = db.relationship("Villager", backref = "islands")

class Image(db.Model):
    """Class to store user images for their profile"""
    __tablename__ = "images"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    image_link = db.Column(db.String, nullable = False)
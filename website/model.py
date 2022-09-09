from website import db
from flask_login import LoginManager, UserMixin
from website import app
import datetime

login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id= db.Column(db.Integer(), primary_key= True)
    username= db.Column(db.String(255))
    email= db.Column(db.String(255))
    phone= db.Column(db.Integer())
    password= db.Column(db.Integer())
    hashed= db.Column(db.String(), unique= True)
    last_name= db.Column(db.String())
    item = db.relationship('Item',
                    backref='user',
                    lazy='dynamic'
                    )
    comment= db.relationship('Comment',
                        backref='user',
                        lazy='dynamic'
                        )

    # @event.listens_for(Engine, "connect")
    # def set_sqlite_pragma(dbapi_connection, connection_record):
    #     cursor = dbapi_connection.cursor()


    def __repr__(self):
        return f"{self.username}"

date=datetime.datetime.now()

class Item(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    category= db.Column(db.String(255))
    items= db.Column(db.Text())
    date= db.Column(db.String(), default=date.strftime('%a %b %Y %I %M'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"{self.category}"



class Comment(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    date= db.Column(db.String(), default= date.strftime('%a %b %Y At- %I:%M'))
    comment= db.Column(db.String(255))
    user_id= db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f"{self.comment}"



db.create_all()
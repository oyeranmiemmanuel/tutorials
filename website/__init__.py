from flask import Flask
from flask_sqlalchemy  import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///user.db'
app.config['SECRET_KEY']='randomtext'
db= SQLAlchemy(app)


from website import route
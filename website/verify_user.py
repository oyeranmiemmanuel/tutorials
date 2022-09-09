from flask import flash, request, url_for, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import login_user, current_user
# from website.dbhelper import DBHelper
from website import app
from website.model import User, db, Item
from flask_mail import Mail, Message
from website.passwordhelper import get_hash, validate_password
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature, BadSignature



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'oyeranmie@gmail.com'
app.config['MAIL_PASSWORD'] = 'ecwvapxdzykiokuf'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail= Mail(app)
s= URLSafeTimedSerializer(app.config['SECRET_KEY'])


def send_link(email):

    token= s.dumps(email, salt='email-confirm')

    #send message to client
    msg= Message('Confirm Email', sender='oyeranmie@email.com', recipients=[email])

    link= url_for('confirm_token', token=token, _external= True)
    msg.body= f'Click on your link to redirect {link}'
    mail.send(msg)



def create_account():
   if request.method == 'POST': 
        email= request.form.get("email")
        firstName= request.form.get("firstName")
        lastName= request.form.get("firstName")
        phone_no= request.form.get("phone")
        password= request.form.get("password")
        password1= request.form.get("password1")


        if len(email) < 5:
            flash("Email is too short", category="error")
        # elif (no_check() in phone):
        #     flash("Phone number must include digits alone", category="error")
        elif (password != password1):
            flash("Password doesn't match", category="error")
        elif (password != password1):
            flash("Password doesn't match", category="error")
        elif len(password) < 6:
            flash("Password too short", category="error")
        elif User.query.filter_by(email=email).first():
            flash("Email Already Exist", category="error")
        elif User.query.filter_by(phone=phone_no).first():
             flash("Number Already Exist", category="error")
        else:
            #add user to database           
            hash= generate_password_hash(password)
            user=User( username=firstName, email=email, password=password, last_name=lastName, phone=phone_no, hashed=hash)
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            return True



def check_login():

    email= request.form.get("userName")
    password= request.form.get("password")
    if len(email) < 0:
        flash("Email cannot be empty", category="error")
        return False

    elif len(password) < 0:
        flash("Password cannot be empty", category="error")
        return False

    else:
        user1= User.query.filter_by(email=email).first()
        if user1 and check_password_hash(user1.hashed, password):
            flash(f"welcome{user1.username}", category='success')
            login_user(user1, remember=True)
            return user1

        else:
            return False



def add_item(category):
    item= request.form.get("item")
    items=Item(category=category, items=item)
    items.user_id= current_user.id
    db.session.add(items)
    db.session.commit() 
    
    print("Added to database")


def confirm_email(email):
    get_user= User.query.filter_by(email=email).first()
    
    if get_user:
        return True 


def reset_user_password(email, password1, password2):
    if password1 == password1:
        salt= generate_password_hash(password2)
        User.query.filter_by(email=email).update({'password':password2, 
                                            'hashed':salt})
        db.session.commit()
    else:
        flash("Password doesn't match", category="error")
from wsgiref.handlers import read_environ
from website import app
from flask import render_template, flash, request
from website.model import User, Item, load_user, Comment
from website.verify_user import *
from flask_login import current_user, login_required, logout_user
from threading import Thread



@app.route("/")
def home():

    return render_template("index.html")




@app.route("/childrens", methods=['POST', 'GET'])
def children_page():
    category= "Childrens Wear"
   
    if request.method == 'POST':
        add_item(category=category)                  
        return render_template("children.html")
        
    else:
        return render_template("children.html")

   
@app.route("/contact")
def contact_page():

    return render_template("contact.html")


@app.route("/fashions", methods=['POST', 'GET'])
def fashion_page():
    if request.method=="POST":
        new_comment= request.form.get('comment')
        if len(new_comment) < 1:
            flash("Comment cannot be empty", category="error")
            comments= Comment.query.all()
            return render_template("fashions.html", comments=comments)
        else:            
            comment=Comment(comment= new_comment)
            comment.user_id= current_user.username
            db.session.add(comment)
            db.session.commit()
            comments= Comment.query.all()


            return render_template("fashions.html", comments=comments)

    else:
        comments= Comment.query.all()


    return render_template("fashions.html", comments=comments)


@app.route("/hoodie", methods=['POST', 'GET'])
def hoodie_page():
    category= "Hoodies"
    if request.method == 'POST':
        add_item(category=category)      
        return render_template("hoodie.html")
        
    else:
        return render_template("hoodie.html")
    


@app.route("/my-items", methods=['POST', 'GET'])
@login_required
def items_page():
    user_id=current_user.id
    get_user= User.query.filter_by(id=user_id).first()
    all_item= get_user.item.all()           
 
    return render_template("user-items.html", Items=all_item)


@app.route("/login", methods=['POST','GET'])
def login_page():
    if request.method == 'POST':
        if check_login():  
            user1= check_login()
            flash(f"welcome {user1.username}", category='success')           
            return redirect(url_for('home'))
        else:
            flash("Username or Password doesn't match", category="error")
            return render_template("log_in.html")


    return render_template('log_in.html')
@app.route("/log-out")
def logout_page():
    logout_user()
    
    return "<p> Logged Out </p>"



@app.route("/mens-wear", methods=['POST', 'GET'])
def mens_page():
    category= "Mens Wear"

   
    if request.method == 'POST':
        add_item(category=category)
                  
        return render_template("mens-wear.html")
        
    else:
        return render_template("mens-wear.html")

@app.route("/native", methods=['POST', 'GET'])
def native_page():
    category= "Native Wear"

    if request.method == 'POST':
        add_item(category=category)          
        return render_template("native.html")
        
    else:
        return render_template("native.html")


@app.route("/not-available")
def not_available():

    return render_template('not-available.html')


@app.route("/forget-password", methods=['POST', 'GET'])
def reset_password():  
    email= request.form.get('email')    
    if request.method=='POST':
        if confirm_email(email):
            send_link(email) 
            print('sent')
            return redirect(url_for('home'))
            

        else:
            return redirect(url_for('reset-password'))

            # return "<h1>Email Incorrect </h1> <a href='/reset-password'> back to previous page </a>" 
  

    return render_template('reset-password.html')



@app.route('/confirm_email/<token>', methods=['POST', 'GET'])
def confirm_token(token):
    
    try:
        email= s.loads(token, salt='email-confirm', max_age=100)
    except SignatureExpired:
        return '<h1> Token Expired </h1> <br/> <a href="/reset-password"> back to previous page </a>'

    except BadTimeSignature:
        return '<h1> Invalid Signature </h1> <br/> <a href="/reset-password"> back to previous page </a>'

    except BadSignature:
        return "<h1> Token Incorrect </h1> <br/> <a href='/reset-password'> back to previous page </a>"

    if request.method=='POST':
        password1= request.form.get('password1')
        password2= request.form.get('password2')
        email= request.form.get('email') 
        reset_user_password(email, password1, password2)
        user= User.query.filter_by(email=email).first()
        login_user(user, remember=True)

        return redirect(url_for('home'))


    return render_template('confirm-password.html') 

    # return render_template('confirm-token.html') 



@app.route("/packs", methods=['POST', 'GET'])
def packs_page():
    category= "Kit Packs"
   
    if request.method == 'POST':
        item=add_item(category=category)

        return render_template("packs.html")
        
    else:
        return render_template("packs.html")


@app.route("/short-nickers", methods=['POST', 'GET'])
def shortnickers_page():
    category= "Short Nickers"
   
    if request.method == 'POST':
        add_item(category=category)
                  
        return render_template("short-nickers.html")
        
    else:
        return render_template("short-nickers.html")


@app.route("/size-guides", methods=['POST', 'GET'])
def size_page():

    return render_template("size_guides.html")

@app.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    if create_account():
        flash("Account Created sucessfully", category="success")
        return redirect(url_for('home'))   

    return render_template("sign-up.html")


@app.route("/sleeves", methods=['POST', 'GET'])
def sleeves_page():
    category= "Sleeves"
   
    if request.method == 'POST':
        add_item(category=category)
                 
        return render_template("sleeves.html")
        
    else:
        return render_template("sleeves.html")


@app.route("/trousers", methods=['POST', 'GET'])
def trousers_page():
    category= "Trouser"

    if request.method == 'POST':
        item=add_item(category=category)

        return render_template("children.html")
        
    else:
        return render_template("trousers.html")


@app.route("/womens-wear")
def womens_page():
    category="Womens Wear"
    if request.method == 'POST':
        item=add_item(category=category)

    return render_template("womens-wear.html")




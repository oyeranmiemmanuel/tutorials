from werkzeug.security import generate_password_hash, check_password_hash
import os
import base64, random


# class PasswordHelper:
def get_hash(password):
    return str(generate_password_hash(password, method='sha512'))

# def get_salt(hash):
#     return  str(hash) + str(random.randint(100, 1000))

def validate_password(hashed, password):
    return check_password_hash(hashed, password)  

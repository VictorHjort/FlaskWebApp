from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/log-in')
def log_in():
    return "<p>Log in</p>"

@auth.route('/log-out')
def log_out():
    return "<p>Log out</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>sign up</p>"
    


    



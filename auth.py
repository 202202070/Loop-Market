from flask import Blueprint


auth=Blueprint('auth', __name__)
   

@auth.route('/login')
def login():
    return " login_Page"


@auth.route("/sign_up")
def sign_up():
    return " sign_up page"
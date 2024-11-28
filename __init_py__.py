from flask import Flask
from flask import Blueprint
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'LOOPmarket@203'


    from views import views
    from auth import auth
    from admin import admin
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/auth")
    app.register_blueprint(admin,url_prefix="/")




    return app
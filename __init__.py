from  flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from todolist.config import Config

db=SQLAlchemy()
bcrypt= Bcrypt()
login_manager= LoginManager()
login_manager.login_view ="users.login" 
login_manager.login_message_category="info"
mail=Mail()

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(Config)

    db.init_app=SQLAlchemy(app)
    bcrypt.init_app= Bcrypt(app)
    login_manager.init_app(app)
    mail.init_app=Mail(app)

    from todolist.users.routes import users
    from todolist.posts.routes import posts
    from todolist.main.routes import main
    from todolist.tasks.routes import tasks
    from todolist.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(tasks)
    app.register_blueprint(errors)

    return app
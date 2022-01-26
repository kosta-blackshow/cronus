import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
                              "sqlite:///" + os.path.join(basedir, "../app.db") + "?check_same_thread=False"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True if os.environ.get("SQLALCHEMY_ECHO") == "True" else False

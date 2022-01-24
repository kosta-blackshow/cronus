from flask import Flask
from backend.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from backend.models import Base

server = Flask(__name__)
server.config.from_object(Config)
db = SQLAlchemy(server, model_class=Base, session_options={'autocommit': False})
migrate = Migrate(server, db)
bootstrap = Bootstrap(server)


from backend import routes, models

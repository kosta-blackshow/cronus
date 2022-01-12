from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

from app.models import Base

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app, model_class=Base)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)

from app import routes, models

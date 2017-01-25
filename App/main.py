from flask import Flask
# from flask import Session

# for api
from App.API.Login import login

# for database
# from App.Models import User

import Models
db = Models.db

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = app.config["APP_SECRET_KEY"]

db.init_app(app)
with app.app_context():
    db.create_all()
# Session(app)

login(app, db)

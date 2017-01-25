from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return "<(User(id='%s', user_name= '%s', password= '%s')>" % (self.user_name, self.password)  # NOQA

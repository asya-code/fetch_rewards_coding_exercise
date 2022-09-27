from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class User(db.Model):
    """Rewards' system user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(75))
    points_total = db.Column(db.Integer)
    # user.transactions through foreign key

    def __repr__(self):
        return f"<user_id={self.user_id}, points={self.points}>"

class Points(db.Model):
    __tablename__ = "points"

    points_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    amount = db.Column(db.Integer)
    payer = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=date.today())

    def __repr__(self):
        return f"<payer={self.payer}, points={self.points}, date={self.date}>"
    

class Payer(db.Model):
    __tablename__ = "payers"

    payer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<payer={self.name}>"

class Transaction(db.Model):
    __tablename__ = "transactions"

    transaction_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    payer = db.Column(db.Integer, db.ForeignKey("payer.payer_id"))
    user = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    points = db.Column(db.Integer, nullable=False)

    user = db.relationship("User", backref="transactions")
    payer = db.relationship("Payer", backref="transactions")

    def __repr__(self):
        return f"<payer={self.payer}, user={self.user}, points={self.points}"


def connect_to_db(app, db_uri="postgresql:///points_tracking", echo=True):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    
    connect_to_db(app)
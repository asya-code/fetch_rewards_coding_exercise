from model import db, User, Payer, Points, Transaction, connect_to_db
from datetime import datetime, date

def create_user(email, password, username, full_name=None, points_total=0):
    """Create and return a new user."""
    user = User(email=email, password=password, username=username, full_name=full_name, points_total=points_total)
    return user

def create_payer(name):
    payer = Payer(name=name)
    return payer

def create_transaction
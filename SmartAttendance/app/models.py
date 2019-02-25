from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login



class User(UserMixin, db.Model):
    email = db.Column(db.String(120), primary_key=True)
    mac_address = db.Column(db.String(120), db.ForeignKey('receiver.mac_address'))
    # with open('templates/myjson.json') as f:    
    #     data = json.load(f)
    #     email = data[0]
    #     MAC = data[1]
    #     print (data)

    def __repr__(self):
        return '<Email {}>'.format(self.email)       

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Receiver(db.Model):
    mac_address = db.Column(db.String(120), primary_key=True)
    time_stamp = db.Column(db.String(120), primary_key=True)
    location_id = db.Column(db.String(120), index=True, unique=True)
    mac = db.relationship('User', backref='Mac', lazy='dynamic')

    def __repr__(self):
        return '<mac_address {}>'.format(self.mac_address)  

@login.user_loader
def load_user(email):
    return User.query.get(email)



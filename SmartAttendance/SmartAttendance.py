from app import app, db
from app.models import User, Receiver

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Receiver': Receiver}
    
#this runs the entire app 

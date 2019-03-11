from os import getenv
from app import create_app
from app.database import db, User

app = create_app(getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)

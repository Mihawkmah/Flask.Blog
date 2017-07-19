from app import db
from datetime import datetime

class User(db.Document):
    meta = {
    'collection': 'user',
    'strict': False
    }
    _id = db.ObjectIdField()
    username = db.StringField(required=True, max_length=64)
    password = db.StringField(max_length=256)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    # TypeError: ObjectId('552f41e56a85f00dd043406b') is not JSON serializable
    def get_id(self):
        return str(self.id)

    def __unicode__(self):
        return self.name


class Posts(db.Document):
    meta = {
    'collection': 'article',
    'strict': False
    }
    title = db.StringField(required=True, max_length=64)
    content = db.StringField(required=True)
    create_time = db.DateTimeField(default=datetime.now)

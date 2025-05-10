from flask_admin.contrib.mongoengine import ModelView
from mongoengine import Document, StringField, DateTimeField
import datetime

# Example model
class Post(Document):
    title = StringField(required=True)
    content = StringField()
    created_at = DateTimeField(default=datetime.datetime.utcnow)

def register_admin_views(admin, db):
    admin.add_view(ModelView(Post))

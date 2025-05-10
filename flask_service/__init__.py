from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    mongo.init_app(app)

    # Register blueprints
    from .upload_service.routes import upload_bp
    from .analytics_service.routes import analytics_bp
    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(analytics_bp, url_prefix='/analytics')

    return app

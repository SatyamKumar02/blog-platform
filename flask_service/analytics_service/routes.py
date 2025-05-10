from flask import Blueprint, request, jsonify, current_app
from flask_service import mongo  # imported from your create_app context
from datetime import datetime

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/', methods=['POST'])
def post_analytics():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    analytics_entry = {
        'post_id': data.get('post_id'),
        'user_id': data.get('user_id'),
        'event': data.get('event'),  # e.g., 'view', 'like', etc.
        'timestamp': datetime.utcnow()
    }

    mongo.db.analytics.insert_one(analytics_entry)

    return jsonify({'status': 'stored'}), 200

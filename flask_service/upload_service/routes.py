from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from upload_service.utils.image_utils import resize_and_optimize_image

upload_bp = Blueprint('upload', __name__)

@upload_bp.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    filename = secure_filename(image.filename)
    upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    image.save(upload_path)
    optimized_path = resize_and_optimize_image(upload_path)

    return jsonify({'url': f"/{optimized_path}"}), 200

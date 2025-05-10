from PIL import Image
import os

def resize_and_optimize_image(filepath, size=(800, 800)):
    img = Image.open(filepath)
    img.thumbnail(size)
    optimized_path = filepath.replace('.', '_optimized.')
    img.save(optimized_path, optimize=True, quality=85)
    return optimized_path

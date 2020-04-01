import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'upload')
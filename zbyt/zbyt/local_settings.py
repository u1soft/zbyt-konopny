import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
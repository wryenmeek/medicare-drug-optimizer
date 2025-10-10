import os

# (Removed sys.path manipulation. Use 'pip install -e .' and let pytest handle imports.)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

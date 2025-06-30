# tests/conftest.py
import sys, os

# ensure project root is on sys.path so tests can import your modules
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root not in sys.path:
    sys.path.insert(0, root)

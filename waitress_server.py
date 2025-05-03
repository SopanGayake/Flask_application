import logging
from waitress import serve
from app import app  # Import the app object from app.py

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Waitress server on http://127.0.0.1:8000")
    # you are using the Waitress WSGI server to serve your Flask application. Waitress is a production-ready WSGI server that is more robust and performant than the built-in Flask development server.
    serve(app, host="127.0.0.1", port=8000)

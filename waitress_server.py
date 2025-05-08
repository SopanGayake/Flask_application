import logging
from waitress import serve
from app import create_app  # Import the create_app function

app = create_app()  # Create the app instance

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Waitress server on http://127.0.0.1:8000")
    serve(app, host="127.0.0.1", port=8000)

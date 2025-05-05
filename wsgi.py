from app import create_app
# The wsgi.py file is typically used to define the entry point for WSGI-compatible web servers to serve your Flask application.
# WSGI (Web Server Gateway Interface) is a specification that allows web servers to communicate with web applications in Python.

app = create_app()

if __name__ == "__main__":
    app.run()  # Enable running this file directly for testing or development

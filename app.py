from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # you are using the built-in Flask development server. This is suitable for development and testing but is not recommended for production use because it is not designed to handle high loads or provide the security features required for a production environment.
    app.run()
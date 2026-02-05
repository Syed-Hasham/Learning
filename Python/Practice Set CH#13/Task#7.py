#pip install flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask Web Server!"

@app.route('/about')
def about():
    return "This is a Flask application."

if __name__ == '__main__':
    app.run(debug=True)

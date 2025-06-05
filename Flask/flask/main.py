from flask import Flask, render_template

''' This script creates a simple Flask application with two routes.
    The first route ('/') returns a welcome message, and the second route ('/index') returns an index page. '''

app = Flask(__name__)
@app.route('/')
def welcome():
    return "<html><body><h1>Welcome to the Flask application!</h1><p>This is a simple Flask app.</p></body></html>"

@app.route('/index')
def index():
    return render_template("index1.html")

if __name__ == '__main__':
    app.run(debug=True)
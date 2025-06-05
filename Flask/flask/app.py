from flask import Flask

''' It creates an instance of Flask class.
    This instance is the WSGI(Web server gateway Interface) application.'''

# This is a WSGI application instance.
# Create an instance of the Flask class.
app = Flask(__name__)

@app.route('/')
def welcome():
    '''This function is a view function that handles requests to the root URL ('/').
       It returns a simple welcome message.'''
    
    return "Welcome to the Flask application!. This is a simple Flask app."

@app.route('/index')
def index():
    return "This is the index page of the Flask application."

# The following block checks if this script is being run directly.
# If it is, it starts the Flask development server.
if __name__ == '__main__':
    # If this script is run directly, start the Flask development server.
    app.run(debug=True)


'''Note: The debug=True option enables the debugger and reloader.
This means that if you make changes to your code, the server will automatically reload.
This is useful during development, but should be turned off in production. '''
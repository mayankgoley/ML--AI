from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask application!"

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index1.html")
    else:
        return "Method not allowed"
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Login Successful! {username}"
    
@app.route('/form', methods = ['GET', 'POST'])
def form():
    return render_template("forms.html")

@app.route('/formdata', methods = ['POST'])
def formdata():
    if request.method == 'POST':
        name = request.form['name']
        return f"Form submitted successfully! Name: {name}"

    
if __name__ =='__main__':
    app.run(debug = True)

##Building URL dymically in Flask using Jinja2
##Variable rules in Flask allow you to pass dynamic values in the URL.
## Jinja 2 is a templating engine for Python that allows you to create dynamic HTML pages.

"""
There are multiple ways to read the data from the backend into the HTML page.
1 - {{}} - expressions to print variables
2 - {% %} - conditional statements
3 - {% for %} - loops to iterate over lists or dictionaries
4 - {#....#}  - comments"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')
def welcome():
    return 'Welcome to the Flask application!'

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'index1.html'
    else:
        return 'Method not allowed'
    
@app.route('/form', methods = ['GET', 'POST'])
def form():
    return render_template('forms.html')

@app.route('/submit_res', methods = ['GET', 'POST'])
def submit_res():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('forms.html')

# Variable rules in Flask allow you to pass dynamic values in the URL.
@app.route('/success/<score>')
def success(score):
    return f'Your score is ' + score

@app.route('/marks/<int:score>')
def marks(score):
    res = ""
    if score >= 30:
        res = 'Congratulations! You have passed the exam.'
    else:
        res = 'Sorry! You have failed the exam.' 
    return render_template('result.html', results = res)

@app.route('/success_route/<int:score>')
def success_route(score):
    if score >=30:
        res = 'PASS'
    else:
        res = 'Fail'
    
    exp = {'score': score, 'result': res}
    
    return render_template('result1.html', results = exp)

@app.route('/final_marks/<int:score>')
def final_marks(score):
    return render_template('result2.html', results=score)

# Create dynamic URL with variable rules

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results = score)


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        Science = float(request.form['Science'])
        Maths = float(request.form['Maths'])
        Data_Science = float(request.form['Data_Science'])
        C = float(request.form['C'])
        total_score = (Science + Maths + Data_Science + C)/ 4
        return redirect(url_for('final_marks', score = total_score))
    return render_template('get_result.html')


    
if __name__ == '__main__':
    app.run(debug=True)
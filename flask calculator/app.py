from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    result = None

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    result = "The result of {} {} {} is: {}".format(num1,operation,num2,result)       
    css = "margin-top:30%;background-color:black; font-family: 'Courier New', Courier, monospace; color: #0082a9;text-align: center"
    return f'<body style="{css}"><h2>{result}</h2></body>'
if __name__ == '__main__':
    app.run(host="0.0.0.0")

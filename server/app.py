#!/usr/bin/env python3

from flask import Flask
import ipdb

app = Flask(__name__)
#ipdb.set_trace()
@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>",200

@app.route('/print/<string:param>')
def sayhello(param):
    print(f'{param}')
    return f'{param}'

@app.route('/count/<int:num>')
def count(num):
    new=''
    for i in range(num):
        new += f'{i}\n'
    return new

@app.route('/math/<int:num1>/<string:ops>/<int:num2>')
def math(num1,ops,num2):
    if ops == '+':
        return str(num1 + num2)
    elif ops == '-':
        return str(num1 - num2)
    elif ops == 'div':
        return  str(num1 / num2)
    elif ops == '%':
        return str(num1 % num2)
    elif ops == '*':
        return str(num1 * num2)


if __name__ == '__main__':
    app.run(port=5555, debug=True)

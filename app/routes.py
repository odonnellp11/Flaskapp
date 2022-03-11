from app import app
from flask import render_template



@app.route('/')
def home():
    print('hello again')
    x = 5
    print(f'X has a value of {x}.')
    return render_template('index.html')

@app.route('/mcfc')
def mechanics_info():
    x = 'mechanics'
    print(f'X has value {x}.')
    return render_template('mechanics.html')
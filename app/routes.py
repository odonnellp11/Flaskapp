from app import app
from flask import render_template



@app.route('/')
def home():
    print('Welcome to Car & Truck Co.')
    x = 'Car & Truck Co.'
    print(f'X has a value of {x}.')
    return render_template('index.html')

@app.route('/mechanics')
def mechanics_info():
    x = 'mechanics'
    print(f'X has value {x}.')
    return render_template('mechanics.html')
from app import app
from flask import render_template



@app.route('/')
def home():
    headline = 'welcome to the Car & Truck Co.'
    return render_template('index.html', headline=headline)

@app.route('/mechanics')
def mechanics_info():
    headline = 'welcome to the Car & Truck Co. Service Dept.'
    mechanics = ['William Bell','Walter Bishop']
    return render_template('mechanics.html', headline=headline, mechanics=mechanics )
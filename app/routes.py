from app import app
from flask import render_template
import requests as r 
@app.route('/')
def home():
    greeting = 'Hello, Enrique'
    print(greeting)
    list_of_duties = ['Pray', 'Code', 'Play the Piano', 'Exercise', 'Date Time', 'Cooking', 'Church Obligations']
    return render_template('index.html', g=greeting, list_of_duties=list_of_duties)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/api-call')
def players():
    data = r.get('https://www.balldontlie.io/api/v1/players?search=')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'broken api'
    full_name = data['data'][0]['first_name'] + ' ' + data['data'][0]['last_name']
    team = data['data'][0]['team']['full_name']
    context = {
        'Name': full_name,
        'Team': team
        
    }
    return render_template('f1.html', **context)


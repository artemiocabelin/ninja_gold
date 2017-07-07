from flask import Flask, request, redirect, render_template, session
import random
import datetime

app = Flask(__name__)

app.secret_key = 'Secret'

@app.route('/')
def index():
    session['activities'] = session.get('activities',[])
    session['gold'] = session.get('gold',0)
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    dateNow = datetime.datetime.now()
    if request.form['building'] == 'farm':
        randomNum = random.randint(10,20)
        building = 'farm'
    elif request.form['building'] == 'cave':
        randomNum = random.randint(5,10)
        building = 'cave'
    elif request.form['building'] == 'house':
        randomNum = random.randint(2,5)
        building = 'house'
    elif request.form['building'] == 'casino':
        randomNum = random.randint(0,50)
        building = 'casino'
    session['gold'] += randomNum
    session['activities'].append('Earned '+str(randomNum)+' golds from the '+building+'! '+str(dateNow)) 

    return redirect('/')

@app.route('/end_session', methods=['POST'])
def end_session():
    session.pop('activities')
    session.pop('gold')
    return redirect('/')

app.run(debug=True)
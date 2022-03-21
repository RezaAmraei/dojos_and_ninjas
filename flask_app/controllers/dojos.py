from dataclasses import dataclass
from flask import render_template, redirect, session, request, flash, Flask
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)


@app.route('/home/create_dojo', methods = ["POST"])
def create_dojo():
    data = {
        "name": request.form['name'],
    }

    Dojo.save(data)
    return redirect('/')
@app.route('/home/new_ninja_page')
def new_ninja_page():
    dojos = Dojo.get_all()
    return render_template('add_ninja.html', all_dojos = dojos)

@app.route('/home/new/ninja', methods=['POST'])
def new_ninja():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    Ninja.save(data)
    return redirect('/')

@app.route('/home/display/<int:id>')
def display_dojo(id):
    data = {
        "dojo_id":id
    }
    dojo = Dojo.get_one(data)
    # print ('---------------------',dojo, '--------------------------')
    for dojos in dojo:
        print('---------------------',dojos, '--------------------------')
    return render_template('show_dojo.html', dojo = dojo)
    

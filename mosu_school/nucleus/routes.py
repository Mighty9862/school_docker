from flask import render_template, request, redirect, flash, url_for

from nucleus import app

@app.route('/')
def home():
    return render_template('index.html', title='Научные школы')

@app.route('/newpage')
def newpage():
    return render_template('newpage.html')

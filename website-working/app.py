from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('main.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['email'] == 'admin@google.com':
		session['logged_in'] = True
	else:
		flash('Wrong password!')
	return home()

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run()
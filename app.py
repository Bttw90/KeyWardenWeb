from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
import secrets

app = Flask(__name__)

# Secret key will protect against modify cookies and cross-site request forgery attacks
foo = secrets.token_urlsafe(16)
app.secret_key = foo

@app.route('/')
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run()
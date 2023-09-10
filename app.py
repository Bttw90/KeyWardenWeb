from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import secrets

app = Flask(__name__)

# Secret key will protect against modify cookies and cross-site request forgery attacks
foo = secrets.token_urlsafe(16)
app.secret_key = foo

@app.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.email.data}.', 'success')
        return redirect(url_for('vault'))
    return render_template('register.html', form = form)

@app.route('/vault')
def vault():
    return render_template('vault.html')

if __name__ == '__main__':
    app.run()
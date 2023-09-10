from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
import secrets
# Temp import
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)

# Secret key will protect against modify cookies and cross-site request forgery attacks
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Temp dict for testing purpose
data_dict = {
    'key1': 'Password1',
    'key2': 'Password2',
    'key3': 'Password3',
}

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

# Temp class
class SelectKeyForm(FlaskForm):
    select_key = SelectField('Select a key', choices=[key for key in data_dict.keys()])

@app.route('/vault', methods = ['GET', 'POST'])
def vault():
    form = SelectKeyForm(data_dict = data_dict)
    selected_value = None

    if form.validate_on_submit():
        selected_key = form.select_key.data
        selected_value = data_dict.get(selected_key, 'Data not found')

    return render_template('vault.html', form = form, selected_value = selected_value)

if __name__ == '__main__':
    app.run()
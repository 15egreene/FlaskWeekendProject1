# our auth blueprint is designed to be a subsection with a specific role within our larger flask app
# we need to connect it, otherwise we wont have access
# tools for routing and blueprint
from flask import Blueprint, render_template, request, redirect, url_for

# create the subsection of application

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth', static_folder='auth_static')

from .authforms import LoginForm

# create first route within blueprint 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    lform = LoginForm()
    if request.method == 'POST':
        if lform.validate_on_submit():
            username = lform.username.data
            password = lform.password.data
            print('formdata:', username, password)
            
            return redirect(url_for('home'))
        else:
            return redirect(url_for('auth.login'))
    return render_template('signin.html', form=lform)
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from app.extensions import db, bcrypt
from app.forms import LoginForm, RegisterForm
from app.models import User

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard_stocks'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard_stocks'))
    return render_template('login.html', form=form)

@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard_stocks'))

    form = RegisterForm()
    if form.validate_on_submit():
        username_taken = User.query.filter_by(username=form.username.data).first()
        if not username_taken:
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('main.login'))

    return render_template('register.html', form=form)

@blueprint.route('/stocks', methods=['GET', 'POST'])
def dashboard_stocks():
    return redirect('/stocks')

@blueprint.route('/options', methods=['GET', 'POST'])
def dashboard_options():
    return redirect('/options')

@blueprint.route('/financials', methods=['GET', 'POST'])
def dashboard_financials():
    return redirect('/financials')

@blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

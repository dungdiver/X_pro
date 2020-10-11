from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditProfileForm
from app.models import User
from app.main import bp


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
# @login_required
def index():
    return render_template('index.html', title='Trang chủ')


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.ho_dem = form.hodem.data
        current_user.ten = form.ten.data
        current_user.nam_gioi = form.namgioi.data
        current_user.nhom_mau = form.nhommau.data
        current_user.dan_toc = form.dantoc.data
        db.session.commit()
        flash('Đã sửa')
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.hodem.data = current_user.ho_dem
        form.ten.data = current_user.ten
        form.nhommau= current_user.nhom_mau
        form.namgioi = current_user.nam_gioi
        form.dantoc = current_user.dan_toc
    return render_template('edit_profile.html', title='Edit Profile', form=form)

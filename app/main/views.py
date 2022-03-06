from flask_login import current_user, login_required
import main
from flask import render_template,request,redirect,url_for,abort
from ..models import User, Pitch
from .forms import UpdateProfile
from .. import db, photos


@main.route('/user/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    word = Pitch.query.filter_by(user = current_user).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,word=word)

@main.route('/')
def index():
    pitches = Pitch.query.all()
    interview = Pitch.query.filter_by(category = 'Interview').all()
    product = Pitch.query.filter_by(category = 'Product').all() 
    project = Pitch.query.filter_by(category = 'Project').all()
    promotion = Pitch.query.filter_by(category = 'Promotion').all() 
    
    return render_template('index.html',pitches = pitches, interview = interview,product = product,project = project, promotion = promotion)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))
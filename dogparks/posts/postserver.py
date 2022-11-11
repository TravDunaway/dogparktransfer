from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import current_user,login_required
from dogparks import db
from dogparks.models import Posts
from dogparks.posts.forms import Postss

userposts = Blueprint('userposts',__name__)

@userposts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = Postss()
    if form.validate_on_submit():
        user_post = Posts(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(user_post)
        db.session.commit()
        flash("Post Created")
        return redirect(url_for('core.index'))

    return render_template('create_post.html',form=form)

@userposts.route('/<int:user_post_id>')
def user_post(user_post_id):
    user_post = Posts.query.get_or_404(user_post_id)
    return render_template('user_post.html',title=user_post.title,
                            date=user_post.date,post=user_post)

@userposts.route("/<int:user_post_id>/update", methods=['GET', 'POST'])
@login_required
def update(user_post_id):
    user_post = Posts.query.get_or_404(user_post_id)
    if user_post.author != current_user:
        abort(403)

    form = Postss()
    if form.validate_on_submit():
        user_post.title = form.title.data
        user_post.text = form.text.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('userposts.user_post', user_post_id=user_post.id))
    elif request.method == 'GET':
        form.title.data = user_post.title
        form.text.data = user_post.text
    return render_template('create_post.html', title='Update',
                           form=form)
@userposts.route("/<int:user_post_id>/delete", methods=['POST'])
@login_required
def delete_post(user_post_id):
    user_post = Posts.query.get_or_404(user_post_id)
    if user_post.author != current_user:
        abort(403)
    db.session.delete(user_post)
    db.session.commit()
    flash("Deleted")
    return redirect(url_for('core.index'))








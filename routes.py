from flask import Blueprint,render_template, url_for, flash, redirect, request, abort
from  todolist import  db
from  todolist.posts.forms import PostForm
from  todolist.models import  Post
from  flask_login import  current_user, login_required

posts=Blueprint("posts", __name__)


@posts.route("/blog/", methods=["GET", "POST"])
@login_required
def blog():
    page=request.args.get("page",1, type=int)
    your_posts=Post.query.filter_by(author=current_user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    image_file =url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("blog.html", title="Your Blog", image_file=image_file, your_posts=your_posts)
    

@posts.route("/post/new", methods=["POST", "GET"])
@login_required
def new_post():
    form=PostForm()   
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user) 
        db.session.add(post)
        db.session.commit()   
        flash("Your post has been created!", "success")
        return redirect(url_for("main.home"))
    image_file =url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("create_post.html",title="New Post", image_file=image_file ,form=form)


@posts.route("/post/<int:post_id>")
def post_content(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template("post_content.html", title=post.title, post=post)

@posts.route("/post/<int:post_id>/yourpost")
@login_required
def your_post_content(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template("your_post_content.html", title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=[ "GET", "POST"])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("main.home"))
    elif request.method =="GET":
        form.title.data=post.title
        form.content.data=post.content
    image_file =url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("update_post.html", title="Update Post", image_file=image_file, form=form)
    
@posts.route("/post/<int:post_id>/delete", methods=["POST", "GET"])
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author !=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash ("Your post has been deleted!", "success")
    return redirect(url_for("posts.blog"))


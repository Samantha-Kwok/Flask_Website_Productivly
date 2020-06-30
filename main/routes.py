from flask import Blueprint, render_template, request
from todolist.models import Task, Post

main=Blueprint("main", __name__)


@main.route("/")
def home():
    page=request.args.get("page", 1, type=int)
    completed_tasks=Task.query.filter_by(complete=True)\
                    .order_by(Task.actual_completion_date.desc())\
                    .limit(20).all()
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page =page ,per_page=5)
    return render_template( "home.html", completed_tasks=completed_tasks, posts=posts)


@main.route("/about")
def  about():
    return render_template("about.html", title ="About")


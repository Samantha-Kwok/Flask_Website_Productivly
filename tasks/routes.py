from datetime import date
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from  todolist import  db
from  todolist.tasks.forms import  TaskForm
from  todolist.models import  Task
from  flask_login import current_user, login_required


tasks=Blueprint("tasks", __name__)



@tasks.route("/todo", methods=["POST","GET"]) 
@login_required
def todo():
    page=request.args.get("page",1, type=int)
    incomplete_tasks=Task.query.filter_by(owner=current_user)\
                    .filter_by(complete=False)\
                    .order_by(Task.end_date.asc())\
                    .paginate(page=page, per_page=15)
    completed_tasks=Task.query.filter_by(owner=current_user)\
                    .filter_by(complete=True)\
                    .order_by(Task.actual_completion_date.desc())\
                    .paginate(page=page, per_page=15)
    image_file =url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template("todo.html", title="To Do List", incomplete_tasks=incomplete_tasks, completed_tasks=completed_tasks, image_file=image_file)


@tasks.route("/task/new", methods=["POST","GET"])
@login_required
def new_task():
    form=TaskForm()
    if form.validate_on_submit():
        task=Task(item=form.item.data, category=form.category.data, start_date=form.start_date.data, end_date=form.end_date.data, owner=current_user)
        db.session.add(task)
        db.session.commit()
        flash("Your task has been created!", "success")
        return redirect(url_for("tasks.todo"))
    return render_template("create_task.html",title="New Task", form=form)

@tasks.route("/task/<int:task_id>/update", methods=[ "GET", "POST"])
@login_required
def update_task(task_id):
    task=Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    form=TaskForm()
    if form.validate_on_submit():
        task.item=form.item.data
        task.category=form.category.data
        task.start_date=form.start_date.data
        task.end_date=form.end_date.data
        db.session.commit()
        flash("Your task has been updated!", "success")
        return redirect (url_for("tasks.todo"))
    elif request.method =="GET":
        form.item.data=task.item
        form.category.data=task.category
        form.start_date.data=task.start_date
        form.end_date.data=task.end_date
    return render_template("Update_task.html", title="Update Task", form=form)


@tasks.route("/task/<int:task_id>")
def your_task_content(task_id):
    task=Task.query.get_or_404(task_id)
    return render_template("your_task_content.html", title="Task", task=task)
    

@tasks.route("/task/<int:task_id>/complete")
@login_required
def complete(task_id):
    task=Task.query.get(task_id)
    task.complete=True
    task.actual_completion_date=date.today()
    db.session.commit()
    return redirect(url_for("main.home"))

@tasks.route("/task/<int:task_id>/delete", methods=["POST", "GET"])
@login_required
def delete_task(task_id):
    task=Task.query.get_or_404(task_id)
    if task.owner!= current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash ("Your task has been deleted!", "success")
    return redirect(url_for("tasks.todo"))


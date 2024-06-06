from flask import Blueprint, request, render_template, flash, redirect
from models.todo import Todo

todo = Blueprint("todo", __name__)


@todo.route("/todo")
def todo_page():
    list = Todo.all()
    return render_template("todo/index.html", todos=list)


@todo.route("/todo/edit", methods=["GET"])
def get_todo_edit_row():
    return render_template("todo/editForm.html", todo={})


@todo.route("/todo/edit", methods=["POST"])
def save_new_todo():
    item = Todo(content=request.form["content"])
    item = item.save_new()
    flash("new task is created!")
    return render_template("todo/rows.html", todos=[todo])


@todo.route("/todo/<id>", methods=["DELETE"])
def delete_todo(id):
    item = Todo(id)
    _ = item.delete()
    flash("task was successfully deleted!")
    return redirect("/todo", 303)


@todo.route("/todo/<id>", methods=["PUT"])
def update_todo(id):
    item = Todo(id)
    print(request.form)
    for data in request.form.items():
        print(data)
        if data[0] == "content":
            item.content = data[1]
        if data[0] == "done":
            item.done = True if data[1] == "True" else False
    item.update()
    flash("task was successfully updated!")
    return redirect("/todo", 303)

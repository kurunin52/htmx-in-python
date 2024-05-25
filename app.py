from flask import Flask, render_template, request, flash
from models.todo import Todo

app = Flask(__name__)
app.secret_key = b"hypermedia journey"


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/books")
def books_page():
    return render_template("books/index.html", todos=list)


@app.route("/todo")
def todo_page():
    list = Todo.all()
    return render_template("todo/index.html", todos=list)


@app.route("/todo/edit", methods=["GET"])
def get_todo_edit_row():
    return render_template("todo/editForm.html", todo={})


@app.route("/todo/edit", methods=["POST"])
def save_new_todo():
    todo = Todo(content=request.form["content"])
    todo = todo.save_new()
    flash("new task is created!")
    return render_template("todo/rows.html", todos=[todo])


@app.route("/todo/<id>", methods=["DELETE"])
def delete_todo(id):
    todo = Todo(id)
    _ = todo.delete()
    flash("task was successfully deleted!")
    return app.redirect("/todo", 303)


@app.route("/todo/<id>", methods=["PUT"])
def update_todo(id):
    todo = Todo(id)
    print(request.form)
    for data in request.form.items():
        print(data)
        if data[0] == "content":
            todo.content = data[1]
        if data[0] == "done":
            todo.done = True if data[1] == "True" else False
    todo.update()
    flash("task was successfully updated!")
    return app.redirect("/todo", 303)


if __name__ == "__main__":
    app.run()

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


if __name__ == "__main__":
    app.run()

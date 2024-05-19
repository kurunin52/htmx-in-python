from flask import Flask, render_template, request, flash
from models.todo import Todo

app = Flask(__name__)
app.secret_key = b"hypermedia journey"


@app.route("/")
def hello_world():
    list = Todo.all()
    return render_template("index.html", todos=list)


@app.route("/edit", methods=["GET"])
def get_edit_row():
    return render_template("editRow.html", todo={})


@app.route("/edit", methods=["POST"])
def save_new():
    todo = Todo(content=request.form["content"])
    todo = todo.save_new()
    flash("new task is created!")
    return render_template("rows.html", todos=[todo])


if __name__ == "__main__":
    app.run()

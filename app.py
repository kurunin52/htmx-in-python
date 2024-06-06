from flask import Flask, render_template
from controllers import todo, books

app = Flask(__name__)
app.secret_key = b"hypermedia journey"
app.register_blueprint(todo.todo)
app.register_blueprint(books.books)


@app.route("/")
def index_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

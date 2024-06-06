from flask import Blueprint, render_template

books = Blueprint("books", __name__)


@books.route("/books")
def books_page():
    return render_template("books/index.html", todos=list)

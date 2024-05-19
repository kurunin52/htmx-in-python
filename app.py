import os
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


CONNECTION_STRING = os.environ.get("AZURE_COSMOS_CONNECTIONSTRING")
client: MongoClient = MongoClient(CONNECTION_STRING)

db = client.get_database("db_todo")
todos = db.todos


@app.route("/")
def hello_world():
    list = todos.find()
    return render_template("index.html", todos=list)


if __name__ == "__main__":
    app.run()

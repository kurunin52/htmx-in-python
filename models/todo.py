import json
from db import db


class Todo:
    def __init__(self, _id=None, content=None, done=False):
        self.id = _id
        self.content = content
        self.done = done

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def save_new(self):
        data = {}
        data["content"] = self.content
        data["done"] = self.done
        result = db.todos.insert_one(data)
        self.id = result.inserted_id
        return self

    def update(self):
        data = {}
        data.content = self.content
        data.done = self.done
        result = db.todos.update_one({"_id": self.id}, {"$set": data})
        self.id = result.upserted_id
        return self

    def delete(self):
        result = db.todos.delete_one({"_id": self.id})
        return result.deleted_count

    @classmethod
    def all(cls):
        items = db.todos.find()
        result = []
        for item in items:
            result.append(Todo(item["_id"], item["content"], item["done"]))
        return result

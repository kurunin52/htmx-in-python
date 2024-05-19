import json


class Todo:
    def __init__(self, id_=None, content=None, done=None):
        self.id = id_
        self.content = content
        self.done = done

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

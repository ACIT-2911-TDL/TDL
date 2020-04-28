from datetime import date


class Task:

    @staticmethod
    def check_type(value, expected_type):
        if not isinstance(value, expected_type):
            raise ValueError(f"Expected type {expected_type}, got {type(value)} instead.")

    def __init__(self, name, description, deadline, complete=False):
        self.check_type(name, str)
        self.check_type(description, str)
        self.check_type(deadline, date)
        self.check_type(complete, bool)
        # set incrementing ID in DB and save it to a variable
        self._name = name
        self._description = description
        self._deadline = deadline
        self.complete = complete

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self.check_type(self, name)
        self._name = name

    def to_dict(self):
        return {"name": self._name, "description": self._description, "deadline": self._description,
                "complete": self.complete}

from datetime import date


class Task:

    @staticmethod
    def check_type(value, expected_type):
        if not isinstance(value, expected_type):
            raise ValueError(f"Expected type {expected_type}, got {type(value)} instead.")

    def __init__(self, name, details, deadline, complete=False):
        self.check_type(name, str)
        self.check_type(details, str)
        self.check_type(deadline, date)
        self.check_type(complete, bool)
        # set incrementing ID in DB and save it to a variable
        self._name = name
        self._details = details
        self._deadline = deadline
        self.complete = complete

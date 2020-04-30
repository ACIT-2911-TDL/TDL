from flask import Flask, make_response, jsonify
from flask_cors import CORS
from task import Task
from datetime import date

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('Tasks/All')
# once the database is running, this will be changed to get the list from there, eliminating the parameter.
def get_all_tasks():
    task_list = []
    task1 = Task("Do Dishes", "Clean them", date(2020, 5, 12))
    task2 = Task("Mow the lawn", "Spinny knife go brrrr", date(2020, 6, 21))
    tasks = [task1, task2]
    for task in tasks:
        task_list.append(task.to_dict())
    return make_response(jsonify(task_list, 400))


if __name__ == '__main__':
    app.run()

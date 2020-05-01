from flask import Flask, jsonify, request, make_response
from task import Task
from database import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

session = sessionmaker(engine)()


def all_tasks():
    tasks = session.query(Task).filter_by(complete=False)
    task_list = []
    for x in tasks:
        x = x.__dict__
        x.pop('_sa_instance_state')
        task_list.append(x)
    return task_list


@app.route('/toDoTasks', methods=["GET"])
def to_do_tasks():
    task_list = []
    for task in all_tasks():
        if not task['complete']:
            task_list.append(task)
    return jsonify(task_list)


@app.route('/doneTasks', methods=["GET"])
def done_tasks():
    task_list = []
    for task in all_tasks():
        if task['complete']:
            task_list.append(task)
    return jsonify(task_list)


@app.route("/newTask", methods=["POST"])
def add_task():
    data = request.json
    data["deadline"] = datetime.strptime(data["deadline"], '%Y-%m-%dT%H:%M')

    try:
        task = Task(name=data["name"], description=data["description"], deadline=data["deadline"])
        session.add(task)
        session.commit()
        return make_response(" ", 204)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route("/deleteTask", methods=["DELETE"])
def delete_task():
    task_id = request.json["task_id"]
    task_to_delete = session.query(Task).filter(Task.id == task_id)
    session.delete(task_to_delete)
    session.commit()


# @app.route("/newTask", methods=["PUT"])
# def update_task():
#     data = request.json
#     try:
#         tasks = session.query(Task).filter(Task.id == data["id"])
#         for t in tasks:
#
#             for item in data_list:
#                 if item:
#                     item.is_vaild = 0
#                     self.session.add(item)  # 加入
#             self.session.commit()



if __name__ == '__main__':
    app.run(debug=True)

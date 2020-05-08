from flask import Flask, jsonify, request, make_response
from task import Task
from database import engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask_cors import CORS
from flask_login import LoginManager
from user import User
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.secret_key = '4z6S8moLNq2YFFUj'
CORS(app)

session = sessionmaker(engine)()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).filter(User.user_id == user_id)


def all_tasks():
    tasks = session.query(Task).all()
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
    try:
        data["deadline"] = datetime.strptime(data["deadline"], '%Y-%m-%dT%H:%M')
        task = Task(name=data["name"], description=data["description"], deadline=data["deadline"])
        session.add(task)
        session.commit()
        return make_response(" ", 204)
    except ValueError as e:
        message = str(e)
        session.rollback()
        return make_response(message, 400)
    
    
@app.route("/CreateUser", methods=["POST"])
def add_user():
    data = request.json
    try:
        user = User(username=data["username"], password=data["password"],
                    firstName=data["firstName"], lastName=data["lastName"], email=data["email"])
        session.add(user)
        session.commit()
        return make_response("", 204)
    except ValueError as e:
        message = str(e)
        print(message)
        session.rollback()
        return make_response(message, 400)
    except IntegrityError:
        message = "Username is already in use, please use another one."
        session.rollback()
        return make_response(message, 400)



@app.route("/deleteTask", methods=["POST"])
def delete_task():
    task_id = request.json["id"]
    task_to_delete = session.query(Task).filter(Task.id == task_id).first()
    session.delete(task_to_delete)
    session.commit()
    return make_response(" ", 204)


@app.route("/completeTask", methods=["POST"])
def update_task():
    task_id = request.json["id"]
    task = session.query(Task).filter(Task.id == task_id).first()
    task.complete = True
    session.add(task)
    session.commit()
    return make_response(" ", 204)

@app.route("/markTask", methods=["POST"])
def mark_task():
    task_id = request.json["id"]
    task = session.query(Task).filter(Task.id == task_id).first()
    task.color = request.json["color"]
    session.add(task)
    session.commit()
    return make_response(" ", 204)


if __name__ == '__main__':
    app.run(debug=True)

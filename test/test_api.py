import requests
from unittest import TestCase


class TestAPI(TestCase):
    def setUp(self) -> None:
        self.data = {"name": "task name", "deadline": "2020-05-05T13:00", "description": "some details"}
        self.return_data = {"name": "task name", "deadline": "2020-05-05T13:00",
                            "description": "some details", "id": "1", "complete": "False"}
        self.return_data2 = {"name": "task name", "deadline": "2020-05-05T13:00",
                             "description": "some details", "id": "2", "complete": "False"}


    def test_add_task_valid(self):
        r = requests.post("http://localhost:5000/newTask", json=self.data)
        r = requests.post("http://localhost:5000/newTask", json=self.data)
        r = requests.post("http://localhost:5000/newTask", json=self.data)

        self.assertEqual(r.status_code, 204)

    def test_add_task_invalid(self):
        data = {"name": "task name", "deadline": "2020-05-05", "description": "some details"}
        r = requests.post("http://localhost:5000/newTask", json=data)
        self.assertEqual(r.status_code, 400)

    def test_to_do_tasks(self):
        r = requests.get("http://localhost:5000/toDoTasks")
        self.assertEqual(r.status_code, 200)

    def test_done_tasks(self):
        r = requests.get("http://localhost:5000/doneTasks")
        self.assertEqual(r.status_code, 200)

    def test_update_task_valid(self):
        r = requests.post("http://localhost:5000/completeTask", json=self.return_data)
        self.assertEqual(r.status_code, 204)

    def test_update_task_invalid(self):
        data = {"name": "task name", "deadline": "2020-05-05T13:00",
                "description": "some details", "id": "100", "complete": "False"}
        r = requests.post("http://localhost:5000/completeTask", json=data)
        self.assertEqual(r.status_code, 500)

    def test_delete_task_valid(self):
        r = requests.post("http://localhost:5000/deleteTask", json=self.return_data2)
        self.assertEqual(r.status_code, 204)

    def test_delete_task_invalid(self):
        data = {"name": "task name", "deadline": "2020-05-05T13:00",
                "description": "some details", "id": "100", "complete": "False"}
        r = requests.post("http://localhost:5000/deleteTask", json=self.data)
        self.assertEqual(r.status_code, 500)
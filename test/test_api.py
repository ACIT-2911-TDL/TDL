from unittest import TestCase
from sqlalchemy import create_engine
import API
from task import Task
import datetime


class TaskTestCase(TestCase):
    def setUp(self) -> None:
        engine = create_engine('mysql+mysqlconnector://root:password@localhost/test')
        task1 = Task(deadline=datetime.datetime.now(),
                     description="Spinny knife go brrrr",
                     name="Mow the lawn")
        task_json = {"deadline": "2020-5-2T08:00",
                     "description": "Spinny knife go brrrr",
                     "name": "Mow the lawn"}

    def tearDown(self) -> None:
        pass

    def CreatingTask(self):
        API.add_task()

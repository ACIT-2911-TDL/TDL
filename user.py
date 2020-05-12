from flask_login import UserMixin
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import PasswordType, force_auto_coercion
from database import engine
from sqlalchemy.orm import sessionmaker


engine.connect()
Base = declarative_base()
Session = sessionmaker(engine)()
force_auto_coercion()


class User(UserMixin, Base):
    __tablename__ = 'user'
    # user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), primary_key=True, nullable=False)
    email = Column(String(20), nullable=False)
    firstName = Column(String(20), nullable=False)
    lastName = Column(String(20), nullable=False)
    password = Column(PasswordType(
        schemes=['pbkdf2_sha512']
    ), nullable=False)


# Drop table in db
# User.__table__.drop(engine)
# create table in db
# User.metadata.create_all(engine)

if __name__ == '__main__':
    new = User(username="123", password="123", firstName="123", lastName="123", email="123@123.com" )
    print(new.__dict__)
    Session.add(new)
    Session.commit()

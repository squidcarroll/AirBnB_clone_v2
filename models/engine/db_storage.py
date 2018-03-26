#!/usr/bin/python3
'''
    Define class DB stroage
'''

from os import getenv

from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session



class DBStorage:
    """
        a connection for the database
    """
    __engine = None
    __session = None
    classes = [User, City, State, Place, Review, Amenity]
    

    def __init__(self):
        self.__engine = create_engine(
        'mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
        pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            output = self.__session.query(*self.classes)
        else:
            output = self.__session.query(cls)
        # do stuff blep

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sesh_maker = sessionmaker(
            bind=self.__engine,
            expire_on_commit=True)
        Session = scoped_session(sesh_maker)
        self.__session = Session()



        


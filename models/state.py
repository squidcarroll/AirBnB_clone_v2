#!/usr/bin/python3
'''
    Implementation of the State class
'''

from os import getenv

# from .city import City
# from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states', cascade='delete')
    else:
        @property
        def cities(self):
            obj_dict = storage.all(City)
            for key, value in obj_dict:
                if value.state_id is not self.id:
                    del obj_dict[key]
            return obj_dict


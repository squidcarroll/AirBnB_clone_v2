#!/usr/bin/python3
'''
    Define the class City.
'''
from models.state import State
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    '''
        Define the class City that inherits from BaseModel.
    '''
    __tablename__ = "cities"
    name = Column(String(128), nulable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nulable=False)

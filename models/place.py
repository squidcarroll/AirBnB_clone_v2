#!/usr/bin/python3
'''
    Define the class Place.
'''
# from models.engine import storage
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


association_table = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False)
)

class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name  = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade='delete')
        amenities = relationship('Amenity',
                                 secondary=association_table,
                                 viewonly=False)
    else:
        @property
        def amenities(self):
            ''' getter for amenity_ids '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            ''' setter for amenity_ids '''
            self.amenity_ids = obj.id
            if obj.__class__.__name__ == "Amenity":
                return
            obj_dict = storage.all(obj)
            for key, value in obj_dict.items():
                if value.place_id == self.id:
                    self.amenity_ids.append(value.id)

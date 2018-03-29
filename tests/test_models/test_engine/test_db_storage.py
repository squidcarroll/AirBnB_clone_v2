#!/usr/bin/python3
''' Tests for db storage '''

from os import getenv
import unittest
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', "wowow")
class TestDbStorage(unittest.testCase):
    ''' tests for db storage '''
    def testAmenity(self):
        amenity = Amenity(name = 'water')
        amenity.save()
        if amenity.id in models.storage.all():
            self.asserTrue(amenity.name, 'water')

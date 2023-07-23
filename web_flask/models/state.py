#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """State class for storing State data"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """Returns the list of City objects from storage linked
               to the current State"""
            from models import storage
            cities_list = []
            all_cities = storage.all('City')
            for city in all_c

#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from models import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    @property
    def cities(self):
        """getter docuemnt"""
        citiesList = []
        citiesAll = storage.all(City)
        for city in citiesAll.values():
            if city.state_id == self.id:
               citiesList.append(city)
        return citiesList

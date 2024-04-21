import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities = relationship between state and city tables.
    """

    __tablename__ = 'states'
    
    # Check storage engine type
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', back_populates='state',
            cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """Returns list of Cities linked to the current State"""
            cities_instances = []
            # Get all cities from storage
            cities_dict = models.storage.all("City")
            # Filter cities linked to the current state
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_instances.append(city)
            return cities_instances


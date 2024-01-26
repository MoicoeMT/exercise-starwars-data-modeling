import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    email = Column(String(50), nullable = False )
    password = Column(String(500), nullable = False )
    profile = relationship("profile")

class Profile(Base):
    __tablename__ = "profile"
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    phone_number = Column(Integer, nullable=True)
    city = Column(String(250), nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    birth_year = Column(String(250), nullable=True)
    eye_color = Column(String(250), nullable=True)
    hair_color = Column(String(250), nullable=True)
    height = Column(Integer, nullable=True)
    favorit = relationship("favorit")

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True)
    diameter = Column(String(250), nullable=True)
    gravity = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    terrain = Column(String(250), nullable=True)
    favorit = relationship("favorit")

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    consumables = Column(String(250), nullable=True)
    manufacturer = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    passengers = Column(Integer, nullable=True)
    terrain = Column(String(250), nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    favorit = relationship("favorit")

class Favorit(Base):
    __tablename__ = "favorit"
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey("people.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

#!/usr/bin/python3
"""Cities Table Model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """Table Declaration"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        unique=True,
        autoincrement=True,
        nullable=False)
    name = Column(
        String(128),
        nullable=False)
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False)
    state = relationship('State')

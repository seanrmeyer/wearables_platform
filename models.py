from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from .database import Base


class Study(Base):
    __tablename__ = "studies"

    study_id = Column(Integer, primary_key=True, index=True)
    study_title = Column(String, unique=True, nullable=True)
    enabled = Column(Boolean, default=True)
    study_url = Column(String)
    study_abstract = Column(String)
    year_published = Column(Integer)
    subject_count = Column(Integer)

   # items = relationship("Subject", back_populates="subject_id")


class Subject(Base):
    __tablename__ = "subjects"

    study_id = Column(Integer)
    subject_id = Column(String, primary_key=True, index=True)

 #   owner = relationship("Study", back_populates="subjects")

class Steps(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    study_id = Column(Integer)
    subject_id = Column(String, ForeignKey("subjects.subject_id"))
    start_time = Column(DateTime)
    steps = Column(Float)

 #   owner = relationship("Study", back_populates="subjects")

class HeartRate(Base):
    __tablename__ = "heart_rate"

    id = Column(Integer, primary_key=True, index=True)
    study_id = Column(Integer)
    subject_id = Column(String, ForeignKey("subjects.subject_id"))
    start_time = Column(DateTime)
    heart_rate = Column(Float)
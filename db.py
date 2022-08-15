# app/db.py

import databases
import ormar
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class Study(ormar.Model):
    class Meta(BaseMeta):
        tablename = "studies"

    study_id: int = ormar.Integer(primary_key=True)
    study_title: str = ormar.String(max_length=255, nullable=True)
    enabled: bool = ormar.Boolean(default=True, nullable=False)

class Subject(ormar.Model):
    class Meta(BaseMeta):
        tablename = "subjects"

    study_id: int = ormar.Integer()
    subject_id: str = ormar.String(max_length=100, primary_key=True)

class Steps(ormar.Model):
    class Meta(BaseMeta):
        tablename = "steps"
    
    id: int = ormar.Integer(primary_key=True)
    study_id: int = ormar.Integer()
    subject_id: str = ormar.String(max_length=100)
    start_time: datetime = ormar.DateTime()
    #end_time: datetime = ormar.DateTime()
    steps: float = ormar.Float()

class HeartRate(ormar.Model):
    class Meta(BaseMeta):
        tablename = "heart_rate"
    
    id: int = ormar.Integer(primary_key=True)
    study_id: int = ormar.Integer()
    subject_id: str = ormar.String(max_length=100)
    start_time: datetime = ormar.DateTime()
    #end_time: datetime = ormar.DateTime()
    heart_rate: int = ormar.Integer()
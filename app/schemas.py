from typing import Union
import datetime
from pydantic import BaseModel


class StudyBase(BaseModel):
    study_id: int
    study_title: str

class Study(StudyBase):
    study_id: int
    study_title: str
    enabled: bool
    study_url = str
    study_abstract = str
    year_published = int
    subject_count = int

    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    study_id: int
    subject_id: str
    #description: Union[str, None] = None

class Subject(SubjectBase):
    subject_id: str
    study_id: int
    #subjects: list[Subject] = []

    class Config:
        orm_mode = True

class StepsBase(BaseModel):
    id: int
    study_id: int
    subject_id: str
    #start_time: datetime
    #steps: float
    #description: Union[str, None] = None

class Steps(StepsBase):
    id: int
    study_id: int
    subject_id: str
    start_time: datetime.datetime
    steps: float
    #subjects: list[Subject] = []

    class Config:
        orm_mode = True

class HeartRateBase(BaseModel):
    id: int
    study_id: int
    subject_id: str
    #start_time: datetime
    #steps: float
    #description: Union[str, None] = None

class HeartRate(HeartRateBase):
    id: int
    study_id: int
    subject_id: str
    start_time: datetime.datetime
    heart_rate: float
    #subjects: list[Subject] = []

    class Config:
        orm_mode = True

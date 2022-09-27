from sqlalchemy.orm import Session

from . import models, schemas


def get_study(db: Session, study_id: int):
    return db.query(models.Study).filter(models.Study.study_id == study_id).first()

def get_studies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Study).offset(skip).limit(limit).all()

def get_subjects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subject).offset(skip).limit(limit).all()

def get_steps(db: Session, study_id: int, skip: int = 0, limit: int = 100):
#    return db.query(models.Steps).offset(skip).limit(limit).all()
    return db.query(models.Steps).filter(models.Steps.study_id == study_id).offset(skip).limit(limit).all()

def get_heartrate(db: Session, study_id: int, skip: int = 0, limit: int = 100):
#    return db.query(models.HeartRate).offset(skip).limit(limit).all()
    return db.query(models.HeartRate).filter(models.HeartRate.study_id == study_id).offset(skip).limit(limit).all()
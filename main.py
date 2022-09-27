from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/studies/", response_model=list[schemas.Study])
def read_studies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    studies = crud.get_studies(db, skip=skip, limit=limit)
    return studies

@app.get("/studies/{study_id}", response_model=schemas.Study)
def read_study(study_id: int, db: Session = Depends(get_db)):
    db_study = crud.get_study(db, study_id=study_id)
    if db_study is None:
        raise HTTPException(status_code=404, detail="Study not found")
    return db_study

@app.get("/subjects/", response_model=list[schemas.Subject])
def read_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subjects = crud.get_subjects(db, skip=skip, limit=limit)
    return subjects

@app.get("/steps/{study_id}", response_model=list[schemas.Steps])
def read_steps(study_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    steps = crud.get_steps(db, study_id=study_id, skip=skip, limit=limit)
    return steps

@app.get("/heart_rate/{study_id}", response_model=list[schemas.HeartRate])
def read_heartrate(study_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    heart_rate = crud.get_heartrate(db, study_id=study_id, skip=skip, limit=limit)
    return heart_rate
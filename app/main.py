# app/main.py

from fastapi import FastAPI

#from app.db import database, User
from app.db import database, Study, Subject, Steps, HeartRate
from sqlalchemy.orm import Session


app = FastAPI(title="MIDAS Wearables Test Platform")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#@app.get("/")
#async def read_root():
#    return await Study.objects.all()


@app.get("/studies_test")
async def read_root():
    return await Study.objects.all()

@app.get("/subjects_test")
async def read_root():
    return await Subject.objects.limit(50).all()

@app.get("/steps_test")
async def read_root():
    return await Steps.objects.limit(50).all()

@app.get("/hr_test")
async def read_root():
    return await HeartRate.objects.limit(50).all()

#@app.get("/studies/{studies}")
#async def read_root():
#    return await Study.objects.all()
#async def read_item(study_id: int):
#    return {"item_id": item_id}

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
 #   await User.objects.get_or_create(email="test@test.com")

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
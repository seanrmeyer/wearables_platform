from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Study(Base):
    __tablename__ = "studies"

    study_id: int = ormar.Integer(primary_key=True)
    study_title: str = ormar.String()
    enabled: bool = ormar.Boolean(default=True)

    study_id = Column(Integer, primary_key=True, index=True)
    study_title = Column(String, max_length=255, nullable=True)
    enabled = Column(Boolean, default=True, nullable=False)

   # items = relationship("Item", back_populates="owner")

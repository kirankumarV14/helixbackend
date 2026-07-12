from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from models.base import Base

class NGO(Base):
    __tablename__ = "ngos"
    id = Column(Integer,primary_key=True,nullable=False,unique=True)
    name = Column(String,nullable=False)
    contact_person = Column(String,nullable=False )
    mobile_number = Column(String,nullable=False,unique=True)
    email = Column(String,nullable=False,unique=True)
    district = Column(String,nullable=False)
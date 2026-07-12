from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Coordinator(Base):
    __tablename__ = "coordinators"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    name = Column(String,nullable=False)
    mobile_number = Column(String,nullable=False,unique=True)
    email = Column(String,nullable=False,unique=True)
    district = Column(String,nullable=False)
    block = Column(String)
    is_active = Column(Boolean)
    
    farmers  = relationship("Farmer",back_populates="coordinator")
    tokens = relationship("Token",back_populates="coordinator")
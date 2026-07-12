from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base 
class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer,primary_key=True,nullable=False,index=True)
    coordinator_id = Column(Integer, ForeignKey("coordinators.id"),nullable=False,index=True)
    
    name = Column(String,nullable=False)
    mobile_number = Column(String,nullable=False,unique=True)
    district = Column(String,nullable=False)
    block = Column(String)
    village = Column(String)
    crop_type = Column(String)
    sowing_date = Column(Date)
    
    plots = relationship("Plot",back_populates="farmer" )
    coordinator = relationship("Coordinator",back_populates="farmers")          #use uselist=False for only one to one relations
    token = relationship("Token", back_populates="farmer",uselist=False)
    
    

    
    
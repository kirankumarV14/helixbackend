from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer,primary_key=True,nullable=False,unique=True,index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"),nullable=False,unique=True)
    coordinator_id = Column(Integer,ForeignKey("coordinators.id"),nullable=False )
    token = Column(String,nullable=False,unique=True)
    is_used = Column(Boolean)
    
    coordinator = relationship("Coordinator",back_populates="tokens")
    farmer = relationship("Farmer",back_populates="token",uselist=False)
    
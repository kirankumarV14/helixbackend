from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Plot(Base):
    __tablename__ = "plots"
    id = Column(Integer,primary_key=True,nullable=False,unique=True,index=True)
    farmer_id = Column(Integer, ForeignKey("farmers.id"),nullable=False,)
    survey_number = Column(String,nullable=False)
    plot_name = Column(String,nullable=False)
    area_acre = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    boundary_geojson = Column(String )
    
    farmer = relationship("Farmer",back_populates="plots")
    
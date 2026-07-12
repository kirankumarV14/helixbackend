from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from models.base import Base

class Otplog(Base):
    __tablename__ = "otp_logs"
    id = Column(Integer,primary_key=True,nullable=False)
    mobile_number = Column(String,nullable=False)
    otp = Column(String)
    attempts = Column(Integer)
    is_verified = Column(Boolean)
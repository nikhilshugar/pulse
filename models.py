from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
from database import Base

# This is the foundational blueprint for all your database models
# Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True, index=True)
    email = Column(String,unique=True,index=True)
    hashed_password = Column(String)
    is_active= Column(Boolean,default=True)
    created_at = Column(DateTime,default=func.now())

class SystemMetric(Base):
    __tablename__ = "system_metric"
    id = Column(Integer,primary_key=True,index=True)
    cpu_percentage = Column(Float,index=True)
    ram_percentage = Column(Float,index=True)
    time_stamp = Column(DateTime,default=func.now())
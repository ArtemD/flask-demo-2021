from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker
import os
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy.orm.session import Session

load_dotenv()

Base = declarative_base()

class License(Base):
    """
    License table object
    """
    __tablename__ = 'licenses'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    postcode = Column(String(255))
    city = Column(String(255))
    license_granting_date = Column(String(255))
    license_type = Column(String(255))
    business_id = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow())

    def __repr__(self):
        """ String representation of the object """
        return f"<License (name='{self.name}', created_at='{self.created_at}')>"

DATABASE_URL = os.environ['DATABASE_URL']
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)

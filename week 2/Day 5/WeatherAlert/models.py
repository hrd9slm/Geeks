from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    humidity = Column(Integer)
    weather_desc = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Table 'weather' créée avec succès.")
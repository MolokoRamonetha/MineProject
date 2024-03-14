from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date,Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pyodbc
Base = declarative_base()


class Tracking_info(Base):
    __tablename__ = 'tracking_info'
    ID = Column(Integer,primary_key=True,autoincrement=True)
    DateColumn = Column(Date)
    TimeColumn = Column(Time)
    Connected_mac = Column(String(255))
    Signal = Column(String(255))
    Raspberry = Column(String(255))
    APName = Column(String(255))
    BussName = Column(String(255))
    APlocation = Column(String(255))

server = '041-L-RAMONMOLO'
database = 'Tracking'
username = 'SA'
password = 'LETHABO'

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
# connection_string = "postgresql://postgres:TipeBonolo@localhost:5433/mine"


engine = create_engine(connection_string, echo=True)
# Base.metadata.drop_all(engine)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


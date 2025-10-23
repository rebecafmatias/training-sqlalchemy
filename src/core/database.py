from sqlalchemy.orm import sessionmaker

from core.models import Base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///product_hub.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def initialize_database():
    
    Base.metadata.create_all(engine)
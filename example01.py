from sqlalchemy import create_engine, delete

engine = create_engine('sqlite:///example01.db', echo=True)

print("Engine created successfully.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

rows_to_insert = [
    User(name='John', age=28),
    User(name='Emma', age=22),
    User(name='Michael', age=35),
    User(name='Alice', age=30),
    User(name='Lucas', age=26)
    ]

delete_stmt = delete(User)

with Session() as session:
    session.execute(delete_stmt)
    session.add_all(rows_to_insert)
    session.commit()

print("New user added successfully.")
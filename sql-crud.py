from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# Create class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Instead of to the database directly, we will ask for a session,
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# Opens an actual session by calling the Session() subclass defined above 
session = Session()

# Creating the database using declarative_base subclass
base.metadata.create_all(db)

# Creating records on our "Programmer" table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="f",
    nationality="British",
    famous_for="First programmer"
)

# Add each instance of our programmers to our session
session.add(ada_lovelace)

session.commit()
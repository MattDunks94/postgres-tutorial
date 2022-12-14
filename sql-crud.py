# Before running programme, session.add each programmer record.
# And session.commit() 

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
    gender="F",
    nationality="British",
    famous_for="First programmer"
)

allan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL Language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

matt_dunks = Programmer(
    first_name="Matt",
    last_name="Dunkerton",
    gender="M",
    nationality="British",
    famous_for="Fingerstyle Guitar"
)

# Add each instance of our programmers to our session (Similar to git add)
# Once the programme has been run, comment out the sessions added,
# so no duplicates
# session.add(ada_lovelace)
# session.add(allan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(matt_dunks)

# Updating a single record (Updating matt_dunks(id=7) famous_for key value)
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# Commit our session to the database. (Similar to git commit)
# session.commit()

# Updating multiple records (Updating gender key value to all programmers)
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# Defensive programming
# if programmer is not None:
#     print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else: 
#         print("Programmer not deleted")
# else:
#     print("No records found")

# Delete multiple records (Demonstration only!!) 
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# Query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
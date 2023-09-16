#!/usr/bin/python3
"""script that lists all City objects
from the database hbtn_0e_101_usa
"""


from sys import argv
from relationship_city import City
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    USR, PASS, DB = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{USR}:{PASS}@localhost:3306/{DB}')
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id)
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
    session.close()

#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

states_table = session.query(State).all()
for obj in states_table:
    print("{}: {}".format(obj.id, obj.name))

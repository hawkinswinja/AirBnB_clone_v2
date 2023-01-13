#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

id='123456'
states = storage.all(State)
print(states.get('State.{}'.format(id)))

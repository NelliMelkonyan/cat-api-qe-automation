from enum import Enum

BASE_URL = 'https://catfact.ninja/'

class Endpoints(Enum):
  FACT = 'fact'
  FACTS = 'facts'
  BREEDS = 'breeds'

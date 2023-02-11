import os
import pickle


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'cards')

with open(os.path.join(DATA_DIR, 'atomic.pickle'), 'rb') as f:
    cards_atomic = pickle.load(f)

with open(os.path.join(DATA_DIR, 'by_set.pickle'), 'rb') as f:
    cards_by_set = pickle.load(f)


a = 20

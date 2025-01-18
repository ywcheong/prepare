import random
from model import Hand

def get_random_hand():
    random_hand_type = random.randint(0, 3)    # bug! random.randint(0, 2) is correct
    return Hand(random_hand_type)
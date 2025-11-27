#Write a generator that randomly yields "Heads" or "Tails"
import random

def coin_flip_generator(iterations):
    for i in range(iterations):
        yield random.choice(['Heads', 'Tails'])

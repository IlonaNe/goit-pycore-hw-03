import random

def get_number_ticket(min, max, quantity):

    if not (1 <=min <= max <= 1000 and quantity <= (max - min + 1)):
        return []
    lottery_numbers = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_numbers)

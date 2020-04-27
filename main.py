import random


def tira_dado():
    return random.randrange(1, 7)
    
d1 = tira_dado()
d2 = tira_dado()
print(d1+d2)
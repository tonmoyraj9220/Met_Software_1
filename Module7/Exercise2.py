import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input(""))
result = roll_dice(sides)
print(result)

while result != sides:
    result = roll_dice(sides)
    print(result)
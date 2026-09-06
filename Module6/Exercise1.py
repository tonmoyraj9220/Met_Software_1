import random
diceCount = int(input("How many dice to roll: "))
sum = 0

for _ in range(diceCount):
    diceRoll = random.randint(1,6)
    sum += diceRoll

print(f"Sum of the dice: {sum}")
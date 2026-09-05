import random
two_digit_code = random.randint(1, 10)

while True:

    guess = int(input("Guess a number (1-10): "))

    if guess > two_digit_code:
            print("Too high")

    elif guess < two_digit_code:
            print("Too low")

    else:
        print("Correct")
        break
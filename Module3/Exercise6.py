import random

three_digit_code = ''.join(str(random.randint(0, 9)) for _ in range(3))

four_digit_code = ''.join(str(random.randint(1, 6)) for _ in range(4))

print("3-digit code: " + three_digit_code)
print("4-digit code: " + four_digit_code)
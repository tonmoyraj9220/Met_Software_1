import random

N = int(input("how many random points to generate: "))

count_inside = 0
generated = 0

while generated < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        count_inside += 1

    generated += 1

pi_approx = 4 * count_inside / N

print(f"Approximation of pi: {pi_approx}")
import numbers

numbers = []

while True:
    number = input("Enter a number: ")
    if number == "":
        break
    numbers.append(float(number))

numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for value in numbers[:5]:
    print(value)
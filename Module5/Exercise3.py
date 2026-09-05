smallest = None
largest = None

while True:
    number = (input("Enter a number (or press Enter to quit): "))

    if number == "":
        print(f"Smallest number: {smallest:0.1f} \nLargest number: {largest:0.1f}")
        break

    number = float(number)
    if smallest is None or number < smallest:
        smallest = number

    if largest is None or number > largest:
        largest = number
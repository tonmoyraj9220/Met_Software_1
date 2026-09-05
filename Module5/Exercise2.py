while True:
    length_in = float(input("Enter length in inches (negative value to quit): "))

    if length_in < 0:
        print("Program ended.")
        break

    if length_in >= 0:
        length_cm = length_in * 2.54
        print(f"{length_in:0.1f} inches is {length_cm:0.2f} centimeters")
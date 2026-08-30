gender = input("Enter biological gender (male/female): ").strip().lower()
hem_value = float(input("Enter hemoglobin value (g/l): "))

low = "Your hemoglobin is low."
normal = "Your hemoglobin is normal."
high = "Your hemoglobin is high."

if gender == "male":
    if hem_value < 134:
        print(low)

    elif 134 <= hem_value <= 167:
        print(normal)

    elif hem_value > 167:
        print(high)

elif gender == "female":
    if 117 > hem_value:
        print(low)

    elif 117 <= hem_value <= 155:
        print(normal)

    elif hem_value > 155:
        print(high)

else:
    print("Invalid gender.")
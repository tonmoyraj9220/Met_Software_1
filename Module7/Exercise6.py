import math

def calculate_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    areaOfPizza = math.pi * radius_m**2
    unit_price = price_euros / areaOfPizza
    return unit_price

d1 = float(input("Enter the diameter of the first pizza (cm): "))
p1 = float(input("Enter the price of the first pizza (euros): "))

d2 = float(input("Enter the diameter of the second pizza (cm): "))
p2 = float(input("Enter the price of the second pizza (euros): "))

unit1 = calculate_unit_price(d1, p1)
unit2 = calculate_unit_price(d2, p2)

print(f"Unit price of the first pizza: {unit1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit2:.2f} euros/m²")

if unit1 < unit2:
    print("The first pizza provides better value for money.")

elif unit2 < unit1:
    print("The second pizza provides better value for money.")

else:
    print("Both pizzas provide the same value for money.")
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talent_to_pound = 20
pound_to_lots = 32
lots_to_grams = 13.3

total_grams = talents * talent_to_pound * pound_to_lots * lots_to_grams + pounds * pound_to_lots * lots_to_grams + lots * lots_to_grams

kilograms = int(total_grams / 1000)
remaining_grams = total_grams % 1000

print(f"The weight in modern units: ")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
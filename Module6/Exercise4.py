names = []

for i in range(5):
    city = input("Enter the name of a city: ")
    names.append(city)

print("\n\nThe cities you entered:")
for city in names:
    print(city)
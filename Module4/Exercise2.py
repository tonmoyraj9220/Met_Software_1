lux = "Upper-deck cabin with a balcony."
a = "Above the car deck, equipped with a window."
b = "Windowless cabin above the car deck."
c = "Windowless cabin below the car deck."

cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

if cabin_class == "LUX":
    print(lux)

elif cabin_class == "A":
    print(a)

elif cabin_class == "B":
    print(b)

elif cabin_class == "C":
    print(c)

else:
    print("Invalid cabin class.")
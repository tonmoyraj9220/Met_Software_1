name = input("\nEnter Player Name: ")
age = int(input("Enter Player Age: "))

print("\nPlayer Name:", name)
print("Player Age:", age)

if age < 12:
    print(f"Sorry {name} you are a minor, so you cannot play this game.")
    
else:
    days_left = 5
    inventory = []

    print(f"\nWelcome to Nature Rescue, {name}!")
    print("The fish in the bay are dying, and nobody knows why.\nCan you find the cause and save the bay?")
    
    command = ""
    while command != "lopeta":
        print("\n----Main Menu----")
        print("\n[1] Start the game")
        print("[2] Check the villege notice board")
        print("[3] Check your backpack")
        print("[4] Rest for the day")
        print("[lopeta] Quit the game")

        command = input("\nChoose an Option - ").strip().lower()

        if command == "1":
            print("\nYou stand in small villege beside the sea, seagulls soaring over your head, \nand a muddy brown river flowing towards the bay.")

        elif command == "2":
            print("\n NOTICE:- Fish found dead on the shore!/nNOTICE:- Strange noises can be heard from the forest upstream!")

        elif command == "3":
            if len(inventory) == 0:
                print("\nYour backpack is empty.")
            else:
                print("\nYour backpack hold:")
                for item in inventory:
                    print("-", item)

        elif command == "4":
            days_left -= 1
            print("\nYou rest. One day passes")
            if days_left == 0:
                print("\nThe festival has arrived and fish in the bay are still dying.")
                print("GAME OVER")
                command = "lopeta"

        elif command == "lopeta":
            print("\nGoodbye", name,"!")

        else:
            print("\nUnknown command, please give an appropriate command")
name = input("\nEnter Player Name: ")
age = int(input("Enter Player Age: "))

print("\nPlayer Name:", name)
print("Player Age:", age)

if age < 12:
    print("You are a minor.")
    
else:
    print("\nWelcome to the adventure game,", name + "!")

    print("\n--- Main Menu ---")
    print("1) explore")
    print("2) inventory")
    print("3) rest")
    print("4) castle")
    print("5) shop")
    print("lopeta = quit")
    print("-----------------")

    while True:
        command = input("Enter a command: ")

        if command == "lopeta":
            print("The game is shutting down. Goodbye!")
            break

        elif command == "explore":
            print("You explore the forest.")

        elif command == "inventory":
            print("Inventory: wooden shield, healing potion, 5 silver coins.")

        elif command == "rest":
            print("Resting under a tree restored your energy.")

        elif command == "castle":
            print("You approach an old castle, the gates creak open slowly.")

        elif command == "shop":
            print("You enter a small shop and the merchant greets you warmly.")

        else:
            print("Unknown command.")

        print("\n--- Main Menu ---")
        print("1) explore")
        print("2) inventory")
        print("3) rest")
        print("4) castle")
        print("5) shop")
        print("lopeta = quit")
        print("-----------------")
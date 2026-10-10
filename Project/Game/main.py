# Import player from the classes file.
from classes import Player

# Import important functions from game_functions file, for game operations.
from game_functions import (
    ask_age, read_file, surroundings, get_weather, status, menu, look_around,
    switch_rooms, pick_up, inventory, test_water, check_endinng, end_game, delete_save,
    save_game, load_game, restore_player
)

# The main function that initiates the game.
def main():
   

    name = input("\nEnter Player Name: ").strip()
    rooms = surroundings()
    player = None

    # load previously saved game
    saved = load_game(name)
    if saved is not None:
        answer = input("A saved game was found. Continue it? (y/n) ").strip().lower()
        if answer == "y":
            player = restore_player(saved, rooms)
            print(f"\nWelcome back, {player.name}!")

    # if player is new
    if player is None:
        age = ask_age()
        if age < 12:
            print(f"\nSorry {name}, you are a minor, so you cannot play this game.")
            return
        player = Player(name, age, rooms["Village"])
        print(f"\nWelcome to Nature Rescue, {name}!")
    
    # Menu
    finished = False
    command = ""
    while command != "exit":
        print()
        status(player)
        menu()
        command = input("\nChoose an option - ").strip().lower()

        if command == "1":
            look_around(player)
        elif command == "2":
            switch_rooms(player)
        elif command == "3":
            pick_up(player)
        elif command == "4":
            inventory(player)
        elif command == "5":
            test_water(player)
        elif command == "6":
            print("\n" + get_weather(player.days_left))
        elif command == "7":
            ending = check_endinng(player)
            if ending is not None:
                end_game(ending)
                finished = True
                command = "exit"
            else:
                print("\nYou are not ready yet. You need the right items in the right place.")
        elif command == "exit":
            print(f"\nGoodbye {player.name}!")
        else:
            print("\nUnknown command, please give an appropriate command.")

        # GameOver
        if player.days_left <= 0 and command != "exit":
            print("\nThe festival day has arrived!")
            ending = check_endinng(player)
            if ending is not None:
                end_game(ending)
            else:
                print("You were not ready and the bay is still dying. GAME OVER")
            finished = True
            command = "exit"

    if finished:
        delete_save(player.name)

    else:
        save_game(player)


main()